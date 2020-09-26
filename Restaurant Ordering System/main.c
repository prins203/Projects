#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<windows.h>
#define MAX 3
#define s 6
//stack
int a[s], b[s];
int top = -1, top1 = -1;
float total=0.0;
//queue
int front = -1;
int rear = -1;
int q[MAX];
//extra design Function
void cls(); //clear screen
void br(int line); //for newline
void pre(int tab);  //for tabspace
void ccolor(int clr);  //for text and background color
void pwellcome();  //for welcome page
int count = 0;
int isfull()
{
    if(top == (s - 1))
        return 1;
    else
        return 0;
}
int isfull1()
{
    if(top1 == (s - 1))
        return 1;
    else
        return 0;
}
int isempty()
{
    if(top == -1)
        return 1;
    else
        return 0;
}
int isempty1()
{
    if(top1 == -1)
        return 1;
    else
        return 0;
}
void push(int b)
{
    if(isfull())
    {
        printf("error");
        return;
    }
    else
    {
        top++;
        a[top] = b;
        return;
    }
}
void push1(int k)
{
    if(isfull1())
    {
        printf("error");
        return;
    }
    else
    {
        top1++;
        b[top1] = k;
        return;
    }
}

int pop()
{
    if(isempty(1))
        printf("error");
    else
        return a[top--];
}
int pop1()
{
    if(isempty1(1))
        printf("error");
    else
        return b[top1--];
}
void insert(int num)
{

	if((rear==MAX-1 && front==0)||(rear==front-1))
			{ccolor(15);printf("\n please display or delete ! \n");}
	else
    {
        if(front == -1)
        {
            front = 0;
        }
        rear = (rear+1)%MAX;
        q[rear]=num;
        ++count;
    }
    if(count==3)
    {
        front = 0;
    }

}
void display()
{
    int i;
    if(front == -1 && rear == -1)
        printf("no choice \n");
    else{
        if(count==3)
        //{if(front<rear)
        {for(i=front;i<=rear;i++)

            printf("%d ",q[i]);
            printf("\n");br(2);pre(2);ccolor(10);
        if(q[0]==1 && q[1]==2 && q[2]==3)
        {
            printf("\"You will die alone and poorly dressed.\" \n");
        }
        else if(q[0]==1 && q[1]==3 && q[2]==2)
        {
            printf("\"Flattery will go far tonight.\" \n");
        }
        else if(q[0]==2 && q[1]==1 && q[2]==3)
        {
            printf("\"He who laughs last is laughing at you. \"\n");
        }
        else if(q[0]==2 && q[1]==3 && q[2]==1)
        {
            printf("\"You will be hungry again in one hour. \"\n");
        }
        else if(q[0]==3 && q[1]==2 && q[2]==1)
        {
            printf("\"You have rice in your teeth.\" \n");
        }
        else if(q[0]==3 && q[1]==1 && q[2]==2)
        {
            printf("\"You think it's a secret, but they know. \"\n");
        }
        else
        {
            printf("Oooops!!! Out of options availaible! try again\n");
        }

    }
    else
        printf("enter 3 items !\n");
    }
    ccolor(12);printf("\n\t\t\t GAME OVER !!!. PLEASE PAY RS. 2 :) \n");
}
   // Update & Insert Function
void insertfirst(int data, char foodname[25], int quantity, float price);
void insertmid(int pos, int data, char foodname[25], int quantity, float price);
void insertend(int data, char foodname[25], int quantity, float price);
void updatefood(int udata, int uquantity);
     // Display Function
void foodlist();
void order_view(int order, int quantity, int or_no);
void main_menu();
//CHECK YOUR FORTUNE
void fortune()
{
    int i,o,n;
    cls();
    int op,op1,op2;
    ccolor(14);printf("HEY ! There are 3 fortune cookies : \n 1.strawberry \n 2.chocolate \n 3.mango \n Enter your preference of flavours according to your taste and get to know your forturne\n");
    ccolor(15);
    do
    {
        ccolor(13);printf("Enter option no. \n 1. insert \n 2.display \n 3. exit \n");
    scanf("%d",&o);
        switch(o)
        {
        case 1:
            ccolor(11);printf("enter a option \n 1.strawberry \n 2.chocolate \n 3.mango \n");
            scanf("%d",&n);
            insert(n);
            break;
        case 2:
            ccolor(10);printf("your preference is : \n");
            display();
             break;
        default:
            exit(1);
        }
    }while(o!=2);
}
//check your understanding
void doubletrouble()
{
    cls();
    int i,n,correct = 0, wrong = 0;
    br(2);pre(2);ccolor(253);printf("DOUBLE TROUBLE\n");
    ccolor(14);br(2);printf("There is a box given and 6 plates with options and their \ncorresponding nos. written on it. Player 1 has to fill the box with plates \naccording to his/her priorities with top priority at top of box that is option \nentered last, hiding from your opponent.");
    ccolor(6);br(2);printf("\nPlayer 2 is not allowed to see, and when player 1 \nhas done, its player 2 turn to write the\npriorities of player 1 according to their \nunderstanding between them.");
    ccolor(7);br(2);pre(2);printf("The options in plates are : \n 1.Friends\n 2.Food \n 3.Money \n 4.Family \n 5.Career \n 6.Yourself");
    ccolor(11);printf("\nEnter 6 no. for player 1 from low  to high priority\n");
    for(i = 0 ; i<6;i++)
    {
        scanf("%d",&n);
        push(n);
    }
    ccolor(11);cls();ccolor(7);br(2);pre(2);
    printf("The options in plates are : \n 1.Friends\n 2.Food \n 3.Money \n 4.Family \n 5.Career \n 6.Yourself");
    printf("\nEnter 6 no. for player 2 from low  to high priority\n");
    for(i = 0 ; i<6;i++)
    {
        scanf("%d",&n);
        push1(n);
    }
    cls();
    for(i=0;i<6;i++)
    {
        if(a[i]==b[i])
        {
            correct++;
        }
        else
            wrong++;
    }
    pre(3);ccolor(14);printf("\nPlayer 1 priorities from top to bottom :\n\n");
    for(i=0;i<6;i++)
    {
        printf(" %d\t",pop());
    }
    br(2);pre(3);ccolor(14);printf("\nPlayer 2 given priorities from top to bottom :\n\n");
    for(i=0;i<6;i++)
    {
        printf(" %d\t",pop1());
    }
    ccolor(12);br(2);pre(2);printf("\n Player 2 has written %d same and %d different choices",correct,wrong);
    ccolor(12);br(1);pre(2);printf("\nSo player 2 points is %d * 10 = %d points\n",correct,correct*10);
    ccolor(7);br(2);pre(2);printf("The options in plates are : \n 1.Friends\n 2.Food \n 3.Money \n 4.Family \n 5.Career \n 6.Yourself \n");
    ccolor(15);br(2);printf("The chart for points : ");
    printf("\n60 = you both have perfect bonding and understanding \n50 = you both are best friends and make a team \n40 = you are good friends\n");
    printf("30 = You both know each other fair \n20 = you need to spend more time together \n10 = you should talk more \n0 = It seems you met today, you need to work more among yourself!");
    pre(3);ccolor(10);printf("\n\n\n\t\tTHANKYOU FOR PLAYING");
}
    //Delete & Count Function
void deletefood(int serial);
int countitem();
    //START Structure Here
struct Node{
    char foodname[50];
	int quantity;
	float price;
	int data;
	struct Node *next;
	};
//Global Type
typedef struct Node node ;
node *head, *list;
int main(){
	system("title  **************HUNGRY MINIONS PROJECT**************** ");
	system("mode con: cols=90 lines=60");
    cls();
	pwellcome();
	Sleep(300);
	cls();
	int c=0;
	int any;
	int cardno[100];
	float cardmoney[100];
	float totalmoney = 0;
	int total_order[100];
	int order_quantity[100];
	int order=0;
	int uquantity;
	int citem;
	head = NULL;
	insertfirst(1,"Hot n Sour soup",100,100.23);
	insertend(2,"Manchow soup",100,80.67);
	insertend(3,"Veg pizza",100,70.83);
	insertend(4,"Burger",100,50.23);
	insertend(5,"Vada pao",100,30.23);
	insertend(6,"Sandwich ",100,30.23);
	insertend(7,"Samosa",100,10.29);
	insertend(8,"Dosa",100,35.13);
	insertend(9,"Chinese sizzler",100,200.13);
    insertend(10,"Hakka Noodles",100,70.67);
	insertend(11,"Banana Smoothie",100,500.83);
	insertend(12,"Minions Sizzler",100,700.23);
	insertend(13,"Cheesy banana fries",100,70.23);
	insertend(14,"Monster shake",100,60.23);
	insertend(15,"Oreo shake",100,100.29);
	insertend(16,"Strawberry cone",100,35.13);
	insertend(17,"Mango cup",100,20.13);
    insertend(18,"Chocolate cone",100,40.13);
    insertend(19,"Orange Bar",100,20.13);
    mainmenu:
	br(1);
    main_menu();
	int main_menu_choice;
	br(1); pre(4); fflush(stdin); scanf("%d",&main_menu_choice);
	if((main_menu_choice >=1 && main_menu_choice <=3)){
		if(main_menu_choice == 1){
			foodlist:
			cls();
			foodlist();
		}
		else if( main_menu_choice == 2){
                char admin_panel_choice[20];
			adminpanelchoicee:
			cls(); br(7) ;   pre(4);  printf("1. Main Menu\n\n\t"); Sleep(300);
            printf("Please Enter Password or ( * to Back in Main Menu ) : ");
			fflush(stdin);  scanf("%s",admin_panel_choice);
			if(strcmp(admin_panel_choice,"heartattack")==0){
				node *temp;
				temp = list;
				adminchoise:
				cls();  br(5); pre(4); printf("You are on Admin Pannel\n\n");
				pre(4);
				printf(" 1. Total Cash Today \n\n");Sleep(250);pre(4);
				printf(" 2. View Card Pay \n\n");Sleep(250);pre(4);
				printf(" 3. Add Food in middle \n\n");Sleep(250);pre(4);
				printf(" 4. Delete Food \n\n");Sleep(250);pre(4);
				printf(" 5. Instant Food List \n\n");Sleep(250);pre(4);
				printf(" 6. Item Counter \n\n");Sleep(250);pre(4);
				printf(" 7. Instant Order Preview\n\n");Sleep(250);pre(4);
				printf(" 8. Add Food at end \n\n");Sleep(250);pre(4);
				printf(" 0. Main Menu \n\n");
				printf("Enter Your Choice From 0-8 : ");
				Sleep(250);
				int adminchoise;
				fflush(stdin);   scanf("%d",&adminchoise);
				if(adminchoise==1){
					cls();  br(7); pre(4);   printf("Todays Total Cash : %0.2f  \n",total);
					Sleep(2000);
					goto adminchoise;
				}
				else if(adminchoise==2){
					if(c!=0){
						cls();  br(3); pre(4);
						printf(" ____________________________\n");pre(4);
						printf("|   Card NO.   |   Money $   |\n");pre(4);
						printf("------------------------------\n");pre(4);
						for(int z=1; z<=c;z++){
							printf("|  %d  | %0.2f |\n",cardno[z],cardmoney[z]);pre(4);
							printf("------------------------------\n");pre(4);
							Sleep(150);
						}
						Sleep(1500);
					}
					if(c==0){
						cls();  br(7); pre(4);
					printf("No Card History\n");}
					Sleep(1500);
					goto adminchoise;
				}
				else if(adminchoise==3){
					foodadd:
					cls();
					char ffoodname[25];
					int fquantity;
					int fdata;
					float fprice;
					int fposi;
					br(3);pre(4);      printf(" Enter Food Name :  ");
					fflush(stdin);     gets(ffoodname);
					fquantity:
					fflush(stdin);
					br(2);pre(4);
					printf(" Enter Food Quantity :  ");
					scanf("%d",&fquantity); fflush(stdin);
                        foodserial:
					br(2);pre(4);  printf(" Enter Food Serial :  ");
                      scanf("%d",&fdata);
                            node *exist;
                            exist = list;
                      while(exist->data!=fdata){
                            if(exist->next==NULL){
                                break;
                            }
                        exist=exist->next;
                      }
                      if(exist->data==fdata){
                       cls(); br(5);pre(3);  printf(" Food Serial Already Exist, Please Re-Enter  "); Sleep(2000);
                       goto foodserial;
                      }
                    fprice:
                      fflush(stdin);
					br(2);pre(4);  printf(" Enter Food Price :  ");fflush(stdin);
					scanf("%f",&fprice);
                     br(2);pre(4);
					printf(" Enter Food Position :  ");
					scanf("%d",&fposi); fflush(stdin);
					br(2);pre(4);  printf("Submiting your data");
					for(int cs=0;cs<4;cs++)
                        {
                            printf(" .");Sleep(500);
                        }
                    insertmid(fposi,fdata,ffoodname,fquantity,fprice);
					br(2);pre(4);      printf("Adding Food  Successfull....\n");
					Sleep(2000);
					goto adminchoise;
				}
				else if(adminchoise==4){
					cls();
					br(7);pre(2);
					printf("Enter Serial No of the Food To Delete : ");
					int fdelete;
					fdeletee:
					fflush(stdin); scanf("%d",&fdelete);
					node *temp;
					temp=list;
					while(temp->data != fdelete){
						temp = temp->next;
					}
					if(temp->data==fdelete){
						deletefood(fdelete);
					}
					else{
						br(2); pre(2); printf("Please Enter Correct Number :  "); Sleep(500);
						goto fdeletee;
					}
                    goto adminchoise;
				}
				else if(adminchoise==5){
					cls();    foodlist(); Sleep(1000);
					br(2);pre(4);  printf("1. <-- back  \n\n");pre(5);
					fflush(stdin);   scanf("%d",&any);
					goto adminchoise;
				}
				else if(adminchoise==6){
					citem = countitem();
					cls();
					for(int cs=1;cs<=citem;cs++){
                    br(7); pre(4);
						printf("Item Counting ");
						printf(" %d ",cs);
						Sleep(150);
						cls();
					}
					cls();
					br(7);pre(4);
					printf("Total Food Item is --> %d  \n",citem); Sleep(2000);
					goto adminchoise;
				}
                  else if(adminchoise==7){
					cls();br(2);pre(2);
					printf("\n\t\t");
					printf("______________________________________________________ ");
					printf("\n\t\t");
					printf("|  Order No.  |   FooD Name   |  Quantity |  In Stock |");
					printf("\n\t\t");
					printf("------------------------------------------------------");
					for(int o=1;o<=order;o++){
						order_view(total_order[o],order_quantity[o],o);
					}
					br(2);pre(4);  printf("1. <-- back  \n\n");pre(5);
					fflush(stdin);   scanf("%d",&any);
					goto adminchoise;
				}
				else if(adminchoise==8){
					foodadd1:
					cls();
					char ffoodname[25];
					int fquantity;
					int fdata;
					float fprice;
					int fposi;
					br(3);pre(4);      printf(" Enter Food Name :  ");
					fflush(stdin);     scanf("%[^\n]s",ffoodname);
					fquantity1:
					fflush(stdin);
					br(2);pre(4);
					printf(" Enter Food Quantity :  ");
					scanf("%d",&fquantity); fflush(stdin);
                        foodserial1:
					br(2);pre(4);  printf(" Enter the last Food Serial: ");
                      scanf("%d",&fdata);
                            node *exist;
                            exist = list;
                      while(exist->data==fdata){
                            if(exist->next==NULL){
                                break;
                            }
                        exist=exist->next;
                      }
                    fprice1:
                      fflush(stdin);
					br(2);pre(4);  printf(" Enter Food Price :  ");fflush(stdin);
					scanf("%f",&fprice);
					br(2);pre(4);  printf("Submiting your data");for(int cs=0;cs<4;cs++){printf(" .");Sleep(500);}
                    insertend(fdata,ffoodname,fquantity,fprice);
					br(2);pre(4);      printf("Adding Food  Successfull....\n");
					Sleep(2000);
					goto adminchoise;
				}
				else if(adminchoise==0){
					goto mainmenu;
				}

				else{
					br(2); pre(4); printf("Please Select From List :  "); Sleep(500);
					goto adminchoise;
				}
                }
               else if(strcmp(admin_panel_choice,"*")==0){
				goto mainmenu;
			}
			else{
				br(2); pre(4);  printf("Please Enter Correct Choice");
				goto adminpanelchoicee;
			}

		}
		else if(main_menu_choice==3){
			cls();
			br(7); pre(3); printf("Thank You For Using Our System \n\n\n\n\n\n\n");
			Sleep(1000);
			exit(1);

		}

	}
	else{
		br(2); pre(4); printf("Please Enter Correct Choice"); Sleep(300);
		goto mainmenu;
	}
	int get_food_choice;
	br(2); fflush(stdin);
	printf("What you wanna eat? Enter its serial no. or enter 0 to go to main menu : ") ;
	scanf("%d",&get_food_choice);
	if(get_food_choice==0){
		goto mainmenu;
	}
	node *temp;
	temp = list ;
	while(temp->data != get_food_choice){
		temp = temp->next;
		if(temp==NULL){
			br(2); pre(4);  printf("Please Choice From List: "); br(2); Sleep(1000);
			goto foodlist;
		}
	}
	if(get_food_choice == temp->data){
		fcquantity:
		br(2); pre(3);
		printf("Enter Food Quantity : ");
		int fcquantity;
		fflush(stdin); scanf("%d",&fcquantity); cls();
		if(fcquantity==0){
			cls(); br(7);pre(3); printf("Quantity Can not be Zero "); Sleep(2000);
			cls();
			goto foodlist;
		}
		else if(fcquantity>temp->quantity){
			cls(); br(7);pre(3); printf("Out of Stock ! "); Sleep(2000);
			goto foodlist;
		}
		int confirm;
       total=total+temp->price*fcquantity;
        br(7);pre(2);  printf("Your choice is:  %s \n\n\t\tIts price is %0.2f \n\n\t\tTotal bill = %0.2f \n\n",temp->foodname,temp->price*fcquantity,total);pre(2);
		printf("1. Confirm to buy this \n\n");pre(2);
		printf("Press 1 to confirm :");
		confirme:
		fflush(stdin); scanf("%d",&confirm);
		if(confirm == 1 ){
			br(2);pre(2);
			printf(" 1. Cash ");
			br(2);pre(2);
            printf(" 2. Credit\n");
            printf("Select Method Of payment 1 or 2: ");
            int payment;
			paymente:
			fflush(stdin);  scanf("%d",&payment);
			if(payment==1){
				total=total+temp->price*fcquantity;
				order++;
				total_order[order]=get_food_choice;
				order_quantity[order]=fcquantity;
				uquantity = temp->quantity - fcquantity;
				updatefood(get_food_choice,uquantity);
				cls();br(7);pre(4);  printf("===>THANK YOU<===");
				ccolor(2);br(2);  printf("Food Ordered Successfully ...");
				ccolor(12);br(2);pre(2);  printf("1. Wanna Buy Another Delicious ? ");
				ccolor(14);br(2);pre(2);  printf("2. Getting bored till food arives? Test your fortune here. \n");
				ccolor(15);br(1);pre(2);  printf("3. Wanna try this game for 2 players till your food is served? \n");
				ccolor(1);br(1);pre(2);  printf("4. Main Menu \n");
				br(2);pre(2);   printf("Select: ");
				int ps_menu;
				psmenue:
				fflush(stdin);  scanf("%d",&ps_menu);
				if(ps_menu==1){goto foodlist;}
				else if(ps_menu==4){goto mainmenu;}
				else if(ps_menu==3){doubletrouble();}
				else if(ps_menu == 2)
                {fortune();}
				else{br(2);pre(4);printf("Please Choice from list : ");
				 goto psmenue;}
			}
			//Credit Card Option
			else if(payment==2){
				int card_number[100];
				c++;
				cls();br(7);pre(4); printf("Enter Your Card No : ");
				fflush(stdin);   scanf("%d",&card_number[c]);
				cardno[c] = card_number[c];
				int pin;
				br(2);pre(2);  printf("Enter Your Card Pin [we never save your pin]  : ");
				fflush(stdin);     scanf("%d",&pin);
				cardmoney[c] = temp->price*fcquantity;
				total=total+temp->price*fcquantity;
				order++;
				total_order[order]=get_food_choice;
				order_quantity[order]=fcquantity;
				uquantity = temp->quantity - fcquantity;
				updatefood(get_food_choice,uquantity);
				br(2);pre(4);  printf("Payment Success...");
				cls();br(7);pre(4);  printf("===>THANK YOU<===");
				ccolor(2);br(2);pre(2);  printf("Food Ordered Successfully ...");
				ccolor(12);br(2);pre(2);  printf("1. Wanna Buy Another Delicious ? ");
				ccolor(14);br(2);pre(2);  printf("2. Getting bored till food arives? Test your fortune here. \n");
                ccolor(15);br(1);pre(2);  printf("3. Wanna try this game for 2 players till your food is served? \n");
				ccolor(1);br(1);pre(2);  printf("4. Main Menu \n");
				int ps_menu2;
				psmenu2e:
				scanf("%d",&ps_menu2);
				if(ps_menu2==1){
                        goto foodlist;}
                else if(ps_menu2==2){fortune();}
                else if(ps_menu2==3){doubletrouble();}
				else if(ps_menu2==4){goto mainmenu;}
				else{br(2);pre(4);printf("Please Choice from list : ");
				 goto psmenu2e;}
			}
			else{
				br(2);pre(4);   printf("Enter Choice from List : ");
				goto paymente;
			}
		}
		else{
			br(2);pre(4);    printf("Enter Choise from List : ");
			goto confirme;
		}  ///end confirm;
	}  ///end get food choice if line
	else{
		br(2);pre(4);  printf("Please Choice From List "); br(2); Sleep(300);
		goto foodlist;
	}  ///end get food choice
	return 0;
}
void cls(){
	system("cls");
}
void br(int line){
	for(int i=0; i<line;i++){
		printf("\n");
	}
}
void pre(int tab){
	for(int i=0; i<tab;i++){
		printf("\t");
	}
}
void main_menu(){
	cls();ccolor(10);
	br(3);pre(2); printf("NOTHING BRINGS PEOPLE TOGETHER LIKE GOOD FOOD ^_^ !! "); Sleep(400);
	br(5); pre(3); printf(" 1. Food Menu"); Sleep(400);
	br(2); pre(3); printf(" 2. Management Panel"); Sleep(400);
	br(2); pre(3); printf(" 3. Exit");  Sleep(400);
	br(1);
}
void insertend(int data, char foodname[25], int quantity, float price){
	node *temp;
	temp=(node *)malloc(sizeof(node));
	temp->data = data ;
	temp->price = price;
	temp-> quantity = quantity;
	strcpy(temp->foodname,foodname);
	temp->next = NULL;
	if(head==NULL){
		head = temp;
		list = head;
	}
	else{
		while(head->next != NULL){
			head = head->next;
		}
		head->next = temp;
	}
}
void insertfirst(int data, char foodname[25], int quantity, float price){
	node *temp;
	temp=(node *)malloc(sizeof(node));
	temp->data = data ;
	temp->price = price;
	strcpy(temp->foodname,foodname);
	temp-> quantity = quantity;
	temp->next = head;
	head = temp;
	list = head ;
}
void insertmid(int pos, int data, char foodname[25], int quantity, float price){
	node *temp,*temp1,*n_node;
    head=list;
	n_node=(node *)malloc(sizeof(node));
    n_node->data = data;
    n_node->price = price;
    n_node-> quantity = quantity;
	strcpy(	n_node->foodname,foodname);
	if(head==NULL)
     {
        head=n_node;
        temp=n_node;
    }
     else
     {
        temp = head;
        for(int i=1;i< pos-1;i++)
        {
            temp = temp->next;
        }
         temp1=temp->next;
        temp->next = n_node;
         n_node->next=temp1;
      }
}
void deletefood(int serial){
	node *temp;
	temp=(node *)malloc(sizeof(node));
	temp = list;
	if(temp->data != serial){
		while(temp->next->data != serial){
			temp = temp->next;
		}
		if(temp->next->data == serial){
			temp->next = temp->next->next;
			cls();
			printf("\n\n\n\n\t\t\tDeleting Item %d ",serial);for(int cs=0;cs<4;cs++){printf(" .");Sleep(400);}
			printf("\n\n\n\n\t\t\tDeleted Successfylly \n"); Sleep(500);
		}
		else{
			printf("\n\n\n\n\t\t\tFood Item Not Found\n"); Sleep(500);
		}
		head = temp ;
	}
	else{
		temp = temp->next;
		cls();
		printf("\n\n\n\n\t\t\tDeleting Item %d ",serial);for(int cs=0;cs<4;cs++){printf(" .");Sleep(400);}
		printf("\n\n\n\n\t\t\tDeleted Successfylly \n"); Sleep(500);
		head = temp ;
		list=head;
	}
}
void updatefood(int udata, int uquantity){
	node *temp;
	temp = list;
	while(temp->data!=udata){
		temp = temp->next;
	}
	if(temp->data == udata){
		temp->quantity = uquantity;
	}
}
int countitem(){
	node *temp;
	temp = list;
	int countitem=0;
	if(temp==NULL){
		countitem = 0;
	}
	else{
		countitem = 1;
		while(temp->next != NULL){
			countitem++;
			temp = temp->next;
		}
	}
	return countitem;
}
void foodlist(){
	ccolor(10);br(2);pre(4);printf("GOOD FOOD IS GOOD MOOD !! ");
	printf("\n\t\t");ccolor(13);
	printf("______________________________________________________ ");
	printf("\n\t\t");
	printf("-------------------------------------------------------");
	node *temp;
	temp = list;
    while(temp != NULL){
        ccolor(7);
        printf("\n\t\t"); ccolor(14);
		printf("|     %d      |    %s  |    %0.2f   |",temp->data,temp->foodname, temp->price);
		ccolor(7);
		printf("\n\t\t"); ccolor(13);
		printf("-------------------------------------------------------");
		temp = temp->next ;
		Sleep(100);
	}
	printf("\n\t\t");ccolor(13);
	printf("_______________________________________________________");
    ccolor(7);
    free(temp);

}
void order_view(int order, int quantity, int or_no){
	node *temp;
	temp = list;
	while(temp->data != order){
		temp = temp->next;
	}
	if(temp->data == order){
		printf("\n\t\t");
		printf("|     %d      |    %s  |     %d     |     %d     |",or_no,temp->foodname,quantity,temp->quantity);
		printf("\n\t\t");
		printf("-------------------------------------------------------");
		Sleep(100);
	}
}
void ccolor(int clr){
	HANDLE  hConsole;
	hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, clr);
}
void pwellcome(){
	ccolor(11);
	char welcome[50]="WELCOME";
	char welcome2[50]=" TO";
	char welcome3[50]=" HUNGRY MINIONS FOOD ORDER";
	char welcome4[50]=" MANAGEMENT SYSTEM";
	printf("\n\n\n\n\n\t\t\t    ");
	for(int wlc=0; wlc<strlen(welcome);wlc++){
		printf(" %c",welcome[wlc]);Sleep(150);
	}
	ccolor(11);
	printf("\n\n\t\t\t\t");
	for(int wlc=0; wlc<strlen(welcome2) ;wlc++){
		printf(" %c",welcome2[wlc]);Sleep(50);
	}
	ccolor(11);
	printf("\n\n\t");
	for(int wlc=0; wlc<strlen(welcome3) ;wlc++){
			printf(" %c",welcome3[wlc]);Sleep(50);
	}
	ccolor(11);
	printf("\n\n\t\t ");
	for(int wlc=0; wlc<strlen(welcome4) ;wlc++){
			printf(" %c",welcome4[wlc]);Sleep(50);
	}
	ccolor(11);
}



