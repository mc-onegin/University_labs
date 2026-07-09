#include <iostream>

struct Node {
        int data;
        Node* prev;
        Node* next;
};

void PushBack(Node* sent, int data)
{
    Node* p = new Node;
    p -> data = data;
    p -> next = sent;
    p -> prev = sent -> prev;
    sent -> prev -> next = p;
    sent -> prev = p;
}

void Print(Node* sent)
{
    Node* p = sent -> next;
    while(p != sent)
    {
        std::cout << p -> data << std::endl;
        p = p -> next;
    }
}

void Clear(Node* sent)
{
    Node* p = sent -> next;
    while(p != sent)
    {
        Node* tmp = p;
        p = p -> next;
        delete tmp;
    }
}

void Duplicate10(Node* sent)
{
    Node* p = sent -> next;
    while(p != sent)
    {
        if(p -> data % 10 == 0)
        {
            Node* q = new Node;
            q -> data = p -> data;
            q -> prev = p;
            q -> next = p -> next;
            p -> next -> prev = q;
            p -> next = q;
            p = p -> next;
        }
        p = p -> next;
    }
}

bool isPrime(int x)
{
    if (x < 2)
        return false;
    for (int d = 2; d <= sqrt(x); d++)
        if(x % d == 0)
            return false;
    return true;
}

void RemovePrime(Node* sent)
{
    Node* p = sent -> next;
    while(p != sent)
    {
        if(isPrime(p -> data))
        {
            Node* tmp = p;
            p -> prev -> next = p -> next;
            p -> next -> prev = p -> prev;
            p = p -> prev;
            delete tmp;
        }
        p = p -> next;
    }
}

int getFirstDigit(int num)
{
    while (num >= 10)
        num /= 10;
    return num;
}

void Sort(Node* sent)
{
    bool flag = false;
    Node* p = sent -> next;
    while(!flag)
    {
        flag = true;
        while(p -> next != sent)
        {
            if(getFirstDigit(p->data) < getFirstDigit(p->next->data))
            {
                int tmp = p->data;
                p->data = p->next->data;
                p->next->data = tmp;
                flag = false;
            }
            p = p->next;
        }
        p = sent -> next;
    }
}

bool lastDigit_2_4(int n)
{
    return (n % 10 == 2 || n % 10 == 4);
}

int main()
{
    Node* sent = new Node;
    sent -> next = sent;
    sent -> prev = sent;

    int n;
    std::cin >> n;
    int cnt = 0;
    int curr;

    for (int i = 0; i < n; i++)
    {
        std::cin >> curr;
        PushBack(sent, curr);
        if(lastDigit_2_4(curr))
            cnt++;
    }
    if(cnt >= 3)
        Sort(sent);
    else
    {
        RemovePrime(sent);
        Duplicate10(sent);
    }
    std::cout << "\n";
    Print(sent);
    Clear(sent);
    delete sent;
}