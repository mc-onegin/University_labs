#pragma once

namespace mt
{
    struct Node
    {
        int data;
        Node* next;
    };
    void PushBack(Node* head, int data);
    void Print(Node* head);
    void Remove(Node*, int index);
    void Clear(Node* head);
    void Make(Node*& head);
    void Sort(Node* head);
    void Double(Node* head, int index);
    int FirstDigit(int t);
    int LastDigit(int t);
    bool Is_2_4_6In(int t);
    bool Is_6_9In(int t);
}
