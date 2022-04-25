#include<time.h>
#include<stdio.h>
#include<stdlib.h>

#include "avl_tree.h"
#include "b_tree.h"
#include "red_black_tree.h"

int op[100][2] = {{0}};
FILE* res;

void insert(int k, FILE*data1, FILE*data2, FILE*data3){
    clock_t t1, t2;
    double t;

    
    t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        fscanf(data1, "%d", &x);
        avl_root = insert_avl(avl_root, x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (avl_tree inserts %d nodes)\n", t, k);
    
    t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        fscanf(data2, "%d", &x);
        insert_b(x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (b_tree inserts %d nodes)\n", t, k);

    t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        fscanf(data3, "%d", &x);
        insert_rb(rb_root,x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (rb_tree inserts %d nodes)\n", t, k);

    fprintf(res, "--------------------------------------------------------\n");
}
void delete(int k,FILE*data1, FILE*data2, FILE*data3){
    clock_t t1, t2;
    double t, t3;
    
    t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        fscanf(data1, "%d", &x);
        avl_root = delete_avl(avl_root, x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (avl_tree deletes %d nodes)\n", t, k);
    
    t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        fscanf(data2, "%d", &x);
        delete_b(x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (b_tree deletes %d nodes)\n", t, k);

     t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        fscanf(data3, "%d", &x);
        delete_rb(rb_root,x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (red_black_tree deletes %d nodes)\n", t, k);

    fprintf(res, "--------------------------------------------------------\n");

}

void search(int k, FILE*data1, FILE*data2, FILE*data3){
    clock_t t1, t2;
    double t;

    t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        avl_node *q;
        fscanf(data1, "%d", &x);
        q = search_avl(avl_root, x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (avl_tree searches %d nodes)\n", t, k);
    
    t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        b_node*q;
        fscanf(data2, "%d", &x);
        q = search_b(b_root,x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (b_tree searches %d nodes)\n", t, k);

     t1 = clock();
    for(int i=0; i<k; i++){
        int x;
        rb_node* q;
        fscanf(data3, "%d", &x);
        q = search_rb(rb_root,x);
    }
    t2 = clock();
    t = (double)(t2 - t1) / CLOCKS_PER_SEC;
    fprintf(res, "%fs (red_black_tree searches %d nodes)\n", t, k);

    fprintf(res, "--------------------------------------------------------\n");
}

int main()
{
    res = fopen("res.txt", "a");
    FILE *data,*data1, *data2, *data3;
    int n, j = 0, i = 0;
    //b initial
    init(3);
    //rb initial
    NI = (rb_node*)calloc(1, sizeof(rb_node));
    NI->lchild = NI->rchild = NI->parent = NULL;
    NI->hue = black;
    rb_root = NI;

    data = fopen("data.txt", "r");
    data1 = fopen("data1.txt", "r");
    data2 = fopen("data2.txt", "r");
    data3 = fopen("data3.txt", "r");
    fscanf(data, "%d", &n);
    for(i = 0; i < n;){
        fscanf(data, "%d", &op[j][0]);
        fscanf(data, "%d", &op[j][1]);
        i += op[j][0];
        j++;
    }
    int k = j-1;
    fprintf(res, "----------------------------------------begin-------------------------------------------------\n");
    while(j--){
        switch(op[k-j][1]){
            case 0:
                insert(op[k-j][0], data1, data2, data3);
                break;
            case 1:
                search(op[k-j][0], data1, data2, data3);
                break;
            case 2:
                delete(op[k-j][0], data1, data2, data3);
                break;
        }
    }
    for(int i=0; i<op[0][0]; i++){
        int x;
        fscanf(data1, "%d", &x);
        avl_root = delete_avl(avl_root, x);
    }

    for(int i=0; i<op[0][0]; i++){
        int x;
        fscanf(data2, "%d", &x);
        delete_b(x);
    }

     for(int i=0; i<op[0][0]; i++){
        int x;
        fscanf(data3, "%d", &x);
        delete_rb(rb_root,x);
    }

    avl_root = NULL;
    b_root = NULL;
    rb_root = NULL;

    data = fopen("data.txt", "w");
    data1 = fopen("data1.txt", "w");
    data2 = fopen("data2.txt", "w");
    data3 = fopen("data3.txt", "w");

    fclose(data);
    fclose(data1);
    fclose(data2);
    fclose(data3);
    
    fprintf(res, "-----------------------------------------end--------------------------------------------------\n\n\n\n");

    fclose(res);
}
