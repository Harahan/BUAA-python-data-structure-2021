#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int key_max;
int key_min;
int mid;

typedef struct b_node{
    int dimension;//key num
    int *key;
    struct b_node **child;
    struct b_node *pa;
}b_node;

b_node *new_b_node(){
    b_node *Node;
    Node = (b_node*)calloc(1, sizeof(b_node));
    if(Node == NULL)return NULL;
    Node->dimension = 0;
    Node->key = (int*)calloc((key_max + 1), sizeof(int));
    if(Node->key == NULL)return NULL;
    Node->child = (b_node**)calloc((key_max + 2), sizeof(b_node*));
    if(Node->child == NULL)return NULL;
    return Node;
}

b_node*b_root = NULL;

void init(int m);
void split(b_node*Node);
void insert_b(int key);
b_node *search_b(b_node *Node, int x);
void do_merge(b_node *left_bro, b_node *right_bro, int mid_temp);
void _merge(b_node *Node);
void _delete(b_node*Node, int id);
void delete_b(int x);
void pre_order_travel_b(b_node *b_root);


void init(int m){
    key_max = m - 1;
    key_min = (m%2)? m/2+1 : m/2;
    mid = m/2;
    b_root = NULL;
}

void split(b_node*Node){
    b_node *pa = NULL, *new_right = NULL;
    while(Node->dimension > key_max){
        int len = Node->dimension;
        new_right = new_b_node();//生成new_right
        if(!new_right)return;
        memcpy(new_right->key, Node->key + mid + 1, (len-mid-1) * sizeof(int));
        memcpy(new_right->child, Node->child + mid + 1, (len-mid) * sizeof(b_node*));
        new_right->dimension = (len-mid-1);
        Node->dimension = mid;//后半部分实际还在
        new_right->pa = Node->pa;
        pa = Node->pa;
        if(!pa){//没有父节点
            pa = new_b_node();
            if(!pa)return;
            b_root = pa;
            pa->child[0] = Node;
            pa->child[1] = new_right;
            Node->pa = pa;
            new_right->pa = pa;
            pa->key[0] = Node->key[mid];
            pa->dimension = 1;
        }else{//有父节点
            int i;
            for(i = pa->dimension; i > 0; i--){
                if(Node->key[mid] < pa->key[i-1]){
                    pa->key[i] = pa->key[i-1];
                    pa->child[i+1] = pa->child[i];//pa->child[i-1] == Node
                }else break;
            }
            pa->key[i] = Node->key[mid];
            pa->child[i+1] = new_right;
            new_right->pa = pa;
            pa->dimension++;
        }
        //删除裂开的部分
        memset(Node->key + mid, 0, (len - mid)*sizeof(int));
        memset(Node->child + mid + 1, 0, (len - mid)*sizeof(b_node*));
        //改new_right->child父节点
        for(int i = 0; i <= new_right->dimension; i++)if(new_right->child[i])new_right->child[i]->pa = new_right;
        Node = pa;
    }
}

void insert_b(int key){
    if(b_root == NULL){
        b_node*Node = new_b_node();
        if(!Node)return;
        Node->dimension = 1;
        Node->key[0] = key;
        Node->pa = NULL;
        b_root = Node;
        return;
    }
    b_node *Node = b_root;
    int i;
    while(Node){
        for(i = 0; i < Node->dimension; i++){
            if(key == Node->key[i])return;
            else if(key < Node->key[i])break;
        }
        if(Node->child[i])Node = Node->child[i];
        else break;
    }
    for(int j = Node->dimension; j > i; j--)Node->key[j] = Node->key[j-1];
    Node->key[i] = key;
    Node->dimension++;
    if(Node->dimension > key_max)split(Node);
}

b_node *search_b(b_node *Node, int x){
    if(!Node)return NULL;
    for(int i = 0; i < Node->dimension; i++){
        if(Node->key[i] == x)return Node;
        else if(Node->key[i] > x)return search_b(Node->child[i], x);
    }
    return search_b(Node->child[Node->dimension], x);
}

void do_merge(b_node *left_bro, b_node *right_bro, int mid_temp){//合并节点
    b_node *pa = left_bro->pa;
    left_bro->key[left_bro->dimension++] = pa->key[mid_temp];
    memcpy(left_bro->key + left_bro->dimension, right_bro->key, right_bro->dimension*sizeof(int));
    memcpy(left_bro->child + left_bro->dimension, right_bro->child, (right_bro->dimension+1)*sizeof(b_node*));
    int i;
    for(i = 0; i <= right_bro->dimension; i++)if(right_bro->child[i])right_bro->child[i]->pa = left_bro;
    left_bro->dimension += right_bro->dimension;
    for(i = mid_temp; i < pa->dimension-1; i++){
        pa->key[i] = pa->key[i+1];
        pa->child[i+1] = pa->child[i+2];
    }
    pa->key[i] = 0;//删除最后一个后补0
    pa->child[i+1] = NULL;
    pa->dimension--;
    free(right_bro->key);
    free(right_bro->child);
    free(right_bro);
    if(pa->dimension < key_max)_merge(pa);
}

void _merge(b_node *Node){//从叶子结点往上调整
    int id, mid_temp;
    b_node *pa = Node->pa;
    b_node *right_bro = NULL, *left_bro = NULL;
    //Node == b_root
    if(!pa){
        if(Node->dimension == 0){
            if(Node->child[0]){//可能不需要
                b_root = Node->child[0];
                Node->child[0]->pa = NULL;
            }else b_root = NULL;
            free(Node->child);
            free(Node->key);
            free(Node);
        }
        return;
    } 
    //Node != b_root
    for(id = 0; id <= pa->dimension; id++)if(pa->child[id] == Node)break;
    if(id > pa->dimension)return;//如果插入有bug
    //Node在pa->child最后
    if(id == pa->dimension){
        mid_temp = id - 1;
        left_bro = pa->child[mid_temp];
        //Node->dimension + left_bro->dimension + 1 <= key_max,要合并节点
        if(Node->dimension + left_bro->dimension + 1 <= key_max)return do_merge(left_bro, Node, mid_temp);//

       if(left_bro->dimension == 1)return;//?
        //Node->dimension + left_bro->dimension + 1 > key_max,采取左补上，上补右
        for(int i = Node->dimension; i > 0; i--){//将pa->key[mid_temp]移到Node->key[0]
            Node->key[i] = Node->key[i-1];
            Node->child[i+1] = Node->child[i];
        }
        Node->child[1] = Node->child[0];

        Node->key[0] = pa->key[mid_temp];
        Node->dimension++;
        Node->child[0] = left_bro->child[left_bro->dimension];//移left_bro->child[left_bro->dimension]
        if(left_bro->child[left_bro->dimension]){
            left_bro->child[left_bro->dimension]->pa = Node;
        }
        //将left_bro->key[left_bro->dimension-1]移到pa->key[mid_temp]
        pa->key[mid_temp] = left_bro->key[left_bro->dimension - 1];
        left_bro->key[left_bro->dimension - 1] = 0;//删除了直接补0
        left_bro->child[left_bro->dimension] = NULL;
        left_bro->dimension--;
        return;
    }
    //Node不在pa->child最后
    mid_temp = id;
    right_bro = pa->child[mid_temp+1];
    //Node->dimension + right_bro->dimension + 1 <= key_max,要合并节点
    if(Node->dimension + right_bro->dimension + 1 <= key_max)return do_merge(Node, right_bro, mid_temp);

    if(right_bro->dimension == 1)return;//?
    //Node->dimension + rightt_bro->dimension + 1 > key_max,采取右补上，上补左
    Node->dimension++;//将pa->key[mid_temp]移到Node->key[dimension+1]
    Node->key[Node->dimension-1] = pa->key[mid_temp];
    Node->child[Node->dimension] = right_bro->child[0];//移right_bro->child[0]
    if(right_bro->child[0]){
        right_bro->child[0]->pa = Node;
    }
    //将rightt_bro->key[0]移到pa->key[mid_temp]
    pa->key[mid_temp] = right_bro->key[0];
    for(int i=0; i <right_bro->dimension; i++){
        right_bro->key[i] = right_bro->key[i+1];
        right_bro->child[i] = right_bro->child[i+1];
    }
    right_bro->child[right_bro->dimension] = NULL;
    right_bro->dimension--;
}

void _delete(b_node*Node, int id){//已经找到要删除的节点，位置
    b_node *o = Node;//o为Node
    b_node *child = o->child[id];
    while(child){
        Node = child;
        child = Node->child[child->dimension];//往下找最大的
    }//删除key在Node上
    if(o != Node) o->key[id] = Node->key[Node->dimension - 1];//如果o不是叶子节点，取叶子节点的最大值替代
    else for(int j = id; j < o->dimension; j++) o->key[j] = o->key[j+1];//是叶子结点直接删除
    Node->key[Node->dimension-1] = 0;
    Node->dimension--;
    if(Node->dimension < key_min)_merge(Node);//调整
}

void delete_b(int x){
    b_node *Node = b_root;
    int i;
    while(Node){
        for(i = 0; i < Node->dimension; i++){
            if(x == Node->key[i]){
                _delete(Node, i);
                return;
            }
            else if(x < Node->key[i])break;
        }
        Node = Node->child[i];
    }
    return;
}

void pre_order_travel_b(b_node *b_root) {
        if(b_root == NULL) return;
        printf("(");
        printf("%d", b_root->key[0]);
        for(int i = 1; i < b_root->dimension; i++) printf(",%d", b_root->key[i]);
        printf(")");
        for(int i = 0; i <= b_root->dimension; i++) pre_order_travel_b(b_root->child[i]);
    }

/*int main()
{
    init(3);

    FILE* data;
    data = fopen("data.txt","r");
    
    int n;
    fscanf(data, "%d", &n);
    while(n--){
        int op, x;
        b_node *q;
        fscanf(data, "%d%d", &op, &x);
        switch (op){
            case 0:
                q = search_b(b_root, x);
                if(!q)printf("Not found!\n");
                else{
                   for(int i = 0; i < q->dimension; i++) if(x == q->key[i]) {
                        printf("%d:%d\n", q->dimension, i);
                        break; 
                    }
                }
                break;
                case 1:
                    insert_b(x);
                    pre_order_travel_b(b_root);
                    printf("\n");
                    break;
                case 2:
                    delete_b(x);
                    pre_order_travel_b(b_root);
                    printf("\n");
                    break;
        }
    }
    fclose(data);
}

*/

