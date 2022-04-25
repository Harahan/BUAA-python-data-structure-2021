#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define red 0
#define black 1

typedef struct rb_node{
    struct rb_node* lchild;
    struct rb_node* rchild;
    struct rb_node* parent;
    int val;
    int hue; // 1 - black  0 - red
}rb_node;


rb_node *rb_root;
rb_node *NI;

rb_node *get_grandparent(rb_node *o){return o->parent->parent;}
rb_node *get_father(rb_node *o){return o->parent;}
rb_node *get_uncle(rb_node *o){
    if(o->parent == NI || get_grandparent(o) == NI) return NI;
    if(o->parent == get_grandparent(o)->lchild) return get_grandparent(o)->rchild;
    else if(o->parent == get_grandparent(o)->rchild) return get_grandparent(o)->lchild;
}

void be_black(rb_node* o){if(o) o->hue = black;}
void be_red(rb_node* o){if(o) o->hue = red;}

//int _max(int a, int b){return a>b?a:b;}
//旋转后，旋转的节点指针仍然指向它，例如本来指针指向的是父亲，旋转之后变成了儿子，指针仍然是指向原来的父亲，现在的儿子，即不需要修改形参的值
void rb_lrotate(rb_node*Node){
    rb_node* temp = Node->rchild;
    Node->rchild = temp->lchild;
    if(temp->lchild != NI) temp->lchild->parent = Node;
    temp->parent = Node->parent;
    if(Node->parent == NI) rb_root = temp;
    else{
        if(Node->parent->lchild == Node) Node->parent->lchild = temp;
        else Node->parent->rchild = temp;
    }
    temp->lchild = Node;
    Node->parent = temp;
}

void rb_rrotate(rb_node*Node){
    rb_node* temp = Node->lchild;
    Node->lchild = temp->rchild;
    if(temp->rchild != NI) temp->rchild->parent = Node;
    temp->parent = Node->parent;
    if(Node->parent == NI) rb_root = temp;
    else{
        if(Node->parent->lchild == Node) Node->parent->lchild = temp;
        else Node->parent->rchild = temp; 
    }
    temp->rchild = Node;
    Node->parent = temp;
}

void insert_fixup(rb_node* Node){
    rb_node* i = Node;
    rb_node* fa = get_father(i);
    rb_node* g = get_grandparent(i);
    while(fa->hue == red){
        rb_node* u = get_uncle(i);
        if(fa == g->lchild){
            //case 1: uncle.hue == red
            //solution: uncle.hue = parent.hue = black, grandparent.hue = red, continue
            if(u->hue == red){
                be_black(u);
                be_black(fa);
                be_red(g);
                i = g;
                fa = get_father(i);
                g = get_grandparent(i);
                continue;
            }
            //case 2: uncle.hue == black(or NI), f.rchild = i
            //solution: rb_lrotate to case 3
            if(fa->rchild == i){
                rb_lrotate(fa);
                rb_node* temp = fa;
                fa= i;
                i = temp;
            }
            //case 3: uncle.hue == black, f.lchild = i
            //solution: f.hue = black, g = red, rb_rrotate
            be_black(fa);
            be_red(g);
            rb_rrotate(g);
        }else{
            //case 1: uncle.hue == red
            //solution: uncle.hue = father.hue = black, grandparent.hue = red, continue
            if(u->hue == red){
                be_black(u);
                be_black(fa);
                be_red(g);
                i = g;
               fa = get_father(i);
                g = get_grandparent(i);
                continue;
            }
            //case 2: uncle.hue = black(or NI), f.lchild = i
            //solution: rb_lrotate to case 3
            if(fa->lchild == i){
                rb_rrotate(fa);
                rb_node* temp = fa;
                fa = i;
                i = temp;
            }
            //case 3: uncle.hue = black(or NI), f.rchild = i
            //solution: f.hue = black, g.hue = red
            be_black(fa);
            be_red(g);
            rb_lrotate(g);
        }
        fa= get_father(i);
        g = get_grandparent(i);
    }
    be_black(rb_root);
}

void insert_rb(rb_node* Node, int key){
    rb_node* i = Node;
    rb_node* fa = NI;
    while(i != NI){
        fa = i;
        if(i->val == key) return;
        else if(key < i->val) i = i->lchild;
        else i = i->rchild;
    }
    i = (rb_node*)malloc(sizeof(rb_node));
    i->parent =fa; i->val = key;
    i->lchild = i->rchild = NI; 
    i->hue = red;
    if(fa!= NI){
        if(i->val < fa->val) fa->lchild = i;
        else fa->rchild = i;
    }else rb_root = i;
    //if(key == 7){pre_order_travel_rb( rb_root); return;}
    insert_fixup(i);
}

rb_node* search_rb(rb_node* Node, int key){
    if(Node == NI) return NULL;
    if(Node->val == key) return Node;
    rb_node *ans;
    if(key < Node->val) ans = search_rb(Node->lchild, key);
    else ans = search_rb(Node->rchild, key);
    return ans;
}

void delete_fixup(rb_node* Node, rb_node* fa){
    rb_node* brother;
    //black + black
    while((Node->hue == black) && Node != rb_root){
        if(fa->lchild == Node){
            brother = fa->rchild;
            //case 1: brother.hue == red
            // solution: dyeing, rb_lrotate to case 2
            if(brother->hue == red){
                brother->hue = black;
                fa->hue = red;
                rb_lrotate(fa);
                brother = fa->rchild;
            }
            //case 2: brother.hue == black, brother's childs are black
            //solution: dyeing, Node to be f, continue
            if((brother->lchild->hue == black)&&(brother->rchild->hue == black)){
                brother->hue = red;
                Node = fa;
                fa = get_father(Node);
                continue;
            }
            //case 3:   brother.hue == black, brother.lchild.hue == red, brother.rchild.hue == black
            //solution: dyeing, rb_lrotate to case 4
            if(brother->rchild->hue == black){
                brother->lchild->hue = black;
                brother->hue = red;
                rb_rrotate(brother);
                brother =fa->rchild;
            }
            //case 4: brother.hue == black,  brother.rchild.hue == red, brother.lchild.hue == black
            //solution: dyeing(father.hue => brother.hue, father.hue = black, brother.rchild.hue = black), rb_lrotate 
            brother->hue = fa->hue;
            fa->hue = black;
            brother->rchild->hue = black;
            rb_lrotate(fa);
            Node = rb_root;
            break;     
        }else{
            brother =fa->lchild;
            //case 1: brother.hue == red
            // solution: dyeing, rb_rrotate to case 2
            if(brother->hue == red){
                brother->hue = black;
                fa->hue = red;
                rb_rrotate(fa);
                brother =fa ->lchild;
            }
            //case 2: brother.hue == black, brother's childs are black
            //solution: dyeing, Node to be f, continue
            if((brother->lchild->hue == black)&&(brother->rchild->hue == black)){
                brother->hue = red;
                Node = fa;
               fa = get_father(Node);
                continue;
            }
             //case 3:   brother.hue == black, brother.rchild.hue == red, brother.lchild.hue == black
            //solution: dyeing, rb_lrotate to case 4
            if(brother->lchild->hue == black){
                brother->rchild->hue = black;
                brother->hue = red;
                rb_lrotate(brother);
                brother =fa->lchild;
            }
            //case 4: brother.hue == black,  brother.lchild.hue == red, brother.rchild.hue == black
            //solution: dyeing(father.hue => brother.hue, father.hue = black, brother.lchild.hue = black), rb_lrotate 
            brother->hue = fa->hue;
            fa->hue = black;
            brother->lchild->hue = black;
            rb_rrotate(fa);
            Node = rb_root;
            break;     
        }
    }
    //case 0: black + red
    //solution: be_black
    if(Node != NI) Node->hue = black;
}

void delete_rb(rb_node* Node, int key){
    rb_node* ch, *fa;
    rb_node* i = Node;
    int hue;
    while(i != NI){
        fa = i;
        if(i->val == key) break;
        if(key < i->val) i = i->lchild;
        else i = i->rchild;
    }
    if(i == NI) return;
    if(i->lchild != NI && i->rchild != NI){
        rb_node* min = i->rchild;
        while(min->lchild != NI) min = min->lchild;

        fa= get_father(i);
        if(fa != NI){
            if(fa->lchild == i) fa->lchild = min;
            else fa->rchild = min;
        }else rb_root = min;
        fa = get_father(min);
        ch = min->rchild;
        hue = min->hue;//删除节点颜色
        if(fa== i) fa= min;
        else{
            if(ch != NI) ch->parent =fa;
            fa->lchild = ch;
            min->rchild = i->rchild;
            i->rchild->parent = min;
        }
        min->parent = i->parent;
        min->lchild = i->lchild;
        i->lchild->parent = min;
        min->hue = i->hue;
        if(hue == black) delete_fixup(ch, fa);//传入替代min的节点，以及min的父节点
        free(i);
        return;
    }
    if(i->lchild != NI) ch = i->lchild;
    else ch = i->rchild;
    fa = get_father(i);
    hue = i->hue;//删除节点颜色
    if(ch != NI) ch->parent = fa;
    if(fa != NI){
        if(fa->lchild == i) fa->lchild = ch;
        else fa->rchild = ch;
    }else rb_root = ch;
    if(hue == black) delete_fixup(ch,fa);//传入替代min的节点，以及min的父节点
    free(i);
}

void pre_order_travel_rb(rb_node* Node){
    if(Node == NI) return;
    printf("(%d, %s) ", Node->val, Node->hue == 1? "black": "red");
    pre_order_travel_rb(Node->lchild);
    pre_order_travel_rb(Node->rchild);
}



/*int main()
{
   NI = (rb_node*)calloc(1, sizeof(rb_node));
   NI->lchild = NI->rchild = NI->parent = NULL;
   NI->hue = black;
   rb_root = NI;

    FILE* data;
    data = fopen("data.txt","r");

   int n;
   fscanf(data, "%d", &n);
   while(n--){
       int op, x;
       rb_node*q;
       fscanf(data, "%d%d", &op, &x);
       switch (op){
            case 0:
                q = search_rb(rb_root, x);
                if(!q) printf("Not found!\n");
                else printf("(%d, %s)\n", q->val, q->hue == 1? "black" : "red");
                break;
            case 1:
                insert_rb(rb_root, x);
                pre_order_travel_rb(rb_root);
                printf("\n");
                break;
            case 2:
                delete_rb(rb_root, x);
                pre_order_travel_rb(rb_root);
                printf("\n");
                break;
       }
   } 
   fclose(data);
}
*/