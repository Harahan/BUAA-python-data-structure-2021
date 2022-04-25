#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct avl_node{
    struct avl_node *lchild;
    struct avl_node *rchild;
    int val;
    int height;
} avl_node;

avl_node* avl_root;

int _max(int a,int b) {
    return a>b?a:b;
}
int height(avl_node *Node){return Node==NULL?0:Node->height;}
void pushup(avl_node **Node){
    (*Node)->height = _max(height((*Node)->lchild), height((*Node)->rchild)) + 1;
}

void avl_lrotate(avl_node **Node){
    avl_node *temp = (*Node)->rchild;
    (*Node)->rchild = temp->lchild;
    temp->lchild = (*Node);
    pushup(Node); pushup(&temp);
    (*Node) = temp;
}

void avl_rrotate(struct avl_node **Node){
    avl_node *temp = (*Node)->lchild;
    (*Node)->lchild = temp->rchild;
    temp->rchild = (*Node);
    pushup(Node); pushup(&temp);
    (*Node) = temp;
}

void LL(avl_node **Node){avl_rrotate(Node);}
void LR(avl_node **Node){avl_lrotate(&((*Node)->lchild)); avl_rrotate(Node);}
void RR(avl_node **Node){avl_lrotate(Node);}
void RL(avl_node **Node){avl_rrotate(&((*Node)->rchild)); avl_lrotate(Node);}

avl_node *insert_avl(avl_node *Node, int key){
    if(Node == NULL){
        Node = (avl_node*)malloc(sizeof(avl_node));
        Node->lchild = Node->rchild = NULL;
        Node->height = 1;
        Node->val = key;
        return Node;
    }
    if(key == Node->val)return Node;
    else if(key < Node->val){
        Node->lchild = insert_avl(Node->lchild, key);
        if (height(Node->lchild) - height(Node->rchild) == 2){
            if(key <= Node->lchild->val) LL(&Node);
            else LR(&Node);
        }
        pushup(&Node);
        return Node;
    }else{
         Node->rchild = insert_avl(Node->rchild, key);
        if (height(Node->rchild) - height(Node->lchild) == 2){
            if(key >= Node->rchild->val) RR(&Node);
            else RL(&Node);
        }
        pushup(&Node);
        return Node;
    }
}

avl_node *search_avl(avl_node *Node, int key){
    if(Node == NULL) return NULL;
    if(Node->val == key)return Node;
    else if(Node->val > key)return search_avl(Node->lchild, key);
    else return search_avl(Node->rchild, key);
}

avl_node *delete_avl(avl_node *Node, int key){
    if(Node == NULL)return NULL;
    if(key < Node->val){
        Node->lchild = delete_avl(Node->lchild, key);
        if(height(Node->rchild) - height(Node->lchild) == 2){
            if(height(Node->rchild->rchild) >= height(Node->rchild->lchild))RR(&Node);
            else RL(&Node);
        }
        pushup(&Node);
        return Node;
    }else if(key > Node->val){
        Node->rchild = delete_avl(Node->rchild, key);
        if(height(Node->lchild) - height(Node->rchild) == 2){
            if(height(Node->lchild->lchild) >= height(Node->lchild->rchild))LL(&Node);
            else LR(&Node);
        }
        pushup(&Node);
        return Node;
    }else{
        if(Node->lchild && Node->rchild){
            if(height(Node->lchild) >= height(Node->rchild)){
                avl_node *p = Node->lchild;
                while(p->rchild)p = p->rchild;
                Node->val = p->val;
                Node->lchild = delete_avl(Node->lchild, p->val);
                pushup(&Node);
                return Node;
            }else{
                avl_node *p = Node->rchild;
                while(p->lchild)p = p->lchild;
                Node->val = p->val;
                Node->rchild = delete_avl(Node->rchild, p->val);
                pushup(&Node);
                return Node;
            }
        }else{
            avl_node*temp;
            temp = Node;
            if(Node->lchild)Node = Node->lchild;
            else if(Node->rchild)Node = Node->rchild;
            else Node = NULL;
            free(temp);
            return Node;
        }
    }
}

void pre_order_travel_avl(avl_node*Node){
    if(Node){
        printf("%d ",Node->val);
        pre_order_travel_avl(Node->lchild);
        pre_order_travel_avl(Node->rchild);
    }
}

/*
int main()
{

    FILE* data;
    data = fopen("data.txt","r");

    int n;
    fscanf(data, "%d", &n);
    while(n--){
        int op, x;
        avl_node*q;
        fscanf(data, "%d%d", &op, &x);
        switch (op){
            case 0:
                q = search_avl(avl_root, x);
                if(!q)printf("Node found!\n");
                else printf("%d %d",q->val, q->height);
                break;
                case 1:
                    avl_root = insert_avl(avl_root, x);
                    pre_order_travel_avl(avl_root);
                    printf("\n");
                    break;
                case 2:
                    avl_root = delete_avl(avl_root, x);
                    pre_order_travel_avl(avl_root);
                    printf("\n");
                    break;
        }
    }
    fclose(data);
}
*/

