#include "func10.hpp"
#include <iostream>
namespace mt
{
    void PushBack(Node* head, int data)
    {
        Node* p = head;
        while (p->next != nullptr)
            p = p->next;

        Node* q = new Node;
        q->data = data;
        q->next = nullptr;
        p->next = q;
    }

    bool Is_2_4_6In(int t)
    {
        while (t > 0)
        {
            if(t % 10 == 2 || t % 10 == 4 || t % 10 == 6)
                return true;
            t /= 10;
        }
        return false;
    }
    bool Is_6_9In(int t)
    {
        while (t > 0)
        {
            if(t % 10 == 6 || t % 10 == 9)
                return true;
            t /= 10;
        }
        return false;
    }

    void Print(Node* head)
    {
        Node* p = head->next;
        while(p != nullptr)
        {
            std::cout << p->data << " ";
            p = p->next;
        }
    }

    void Remove(Node* head, int index)
    {
        Node* p = head;
        int i = 0;
        while(p->next != nullptr && i != index)
        {
            i++;
            p = p->next;
        }
        if(p->next == nullptr)
            return;
        
        Node* tmp = p->next;
        p->next = p->next->next;
        delete tmp;
    }

    void Clear(Node* head)
    {
        Node* p = head;
        while(p->next != nullptr)
        {
            Node* tmp = p->next;
            p = p->next;
            delete tmp;
        }
    }

    void Make(Node*& head)
    {
        head = new Node {0, nullptr};
    }

    int FirstDigit(int t)
    {
        while(t > 9)
        {
            t/=10;
        }
        return t;
    }

    int LastDigit(int t)
    {
        return t % 10;
    }

    void Sort(Node* head)
    {
        bool flag = false;
        Node* p = head;
        while(!flag)
        {
            flag = true;
            while(p->next != nullptr)
            {
                if(p->data > p->next->data)
                {
                    int tmp = p->data;
                    p->data = p->next->data;
                    p->next->data = tmp;
                    flag = false;
                }
                p = p->next;
            }
            p = head;
        }
    }

    void Double(Node* head, int index)
    {
        Node* p = head;
        int i = 0;
        while(p->next != nullptr && i != index)
        {
            i++;
            p = p->next;
        }
        if(p->next == nullptr)
            return;
        
        Node* tmp = new Node();
        tmp->data = p->next->data;
        tmp->next = p->next;
        p->next = tmp;
    }
}

