#include "func10.hpp"
#include <iostream>

int main()
{
    bool flag1 = true;
    bool flag2 = true;
    using namespace mt;
    Node* head;
    Make(head);
    int n, prevEl, currEl;
    std::cin >> n;
    std::cin >> prevEl;
    PushBack(head, prevEl);
    for(int i = 1; i < n; i++)
    {
        std::cin >> currEl;
        PushBack(head, currEl);
        if (FirstDigit(prevEl) > FirstDigit(currEl)) 
            flag1 = false;
        if (LastDigit(prevEl) > LastDigit(currEl))
            flag2 = false;
        prevEl =  currEl;
    }

    if(flag1 || flag2)
    {
        Node* p = head;
        int i = 0;
        while(p->next != nullptr)
        {

            if (!Is_2_4_6In(p->next->data))
            {
                Node* tmp = p->next;
                p->next = p->next->next;
                delete tmp;
                //Remove(head, i);
                i--;
            } 
            else if(Is_6_9In(p->next->data))
            {
                Node* tmp = new Node();
                tmp->data = p->next->data;
                tmp->next = p->next;
                p->next = tmp;
                //Double(head, i);
                i++;
                p = p->next->next;
            } 
            else
                p = p->next;
            i++;
        }
    }
    else
    {
        Sort(head);
    }
    Print(head);
    Clear(head);

    return 0;
}