#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

const int N_MAX=2000;

bool Read (int& n, std::string words[N_MAX])
{
    std::ifstream in("input2.txt");
    if (!in.is_open())
    {
        std::cerr<<"File error"<<std::endl;
        return false;
    }
    n=0;
    while (!in.eof())
    {
        in>> words[n];
        for(int j = 0; j < words[n].length(); j++)
        {
            if(ispunct(words[n][j]))
            {
                words[n].erase(j, 1);
                j--;
            }
        }
        n++;
    }
    return true;
}

bool isPalindrome( int n, std::string words[N_MAX]) 
{   
    for (int i=0; i<n; i++)
    {
        if(words[i].length()>2)
        {
            std::string reversed = words[i];
            std::reverse(reversed.begin(), reversed.end());
            if (words[i] == reversed)  
                return true;
            continue;
        }
    }
    return false;
}

void part_vowels(int n,  std::string words[N_MAX])
{
    float part;
    float mas_part[N_MAX];
    std::string vowels = "aeiouyAEIOUY"; 
    for (int i = 0; i < n; i++)
    {
        int vowelCount = 0; 
        for (int m = 0; m < words[i].length(); m++)
        {
            words[i][m] = tolower(words[i][m]);
            if(words[i][m] == 'a' || words[i][m] == 'e' || words[i][m] == 'i' || words[i][m] == 'o' || words[i][m] == 'u' || words[i][m] == 'y')
                vowelCount++; 
        }
        part = (float)vowelCount/(float)(words[i].length());
        mas_part[i] = part;
        std::cout << mas_part[i] << " " << words[i] <<  std::endl;
    }
    for(int j = 0; j < n; j++)
    {
        for(int k = j + 1; k < n; k++)
        {
            if(mas_part[j] < mas_part[k])
            {
                std::string tmp = words[j];
                words[j] = words[k];
                words[k] = tmp;

                float tmp1 = mas_part[j];
                mas_part[j] = mas_part[k];
                mas_part[k] = tmp1;
            }
        }
    }
}


void write1(int n,  std::string words[N_MAX] )
{ 
    
    for (int i=0; i<n; i++)
    {
        std::ofstream out("output2.txt");
        if(!out.is_open())
        {
            std::cerr<<"File error"<<std::endl;
        }
        for(int i = 0; i < n; i++)
        {
            out << words[i] << std::endl;
        }
    }

}
void delete_vowels_double_consonants(int n, std::string words[N_MAX], std::string new_words[N_MAX])
{
    int k=0;
    std::string result; 
    std::string vowels = "aeiouyAEIOUY";
    for (int i=0; i<n;i++)
    {
        result="";
        for (char c : words[i]) 
        {
            if (vowels.find(c) == std::string::npos) 
            {
                result += c; 
                result += c;
            }
        }
        new_words[k]=result;
        k++;
    }
}

void write2(int n, std::string new_words[N_MAX])
{
    std::sort(new_words, new_words + n);
    for(int i = 0; i < n; i++)
    {
        if(new_words[i].length() == 0)
        {
            for(int j = i; j < n; j++)
            {
                new_words[j] = new_words[j + 1];
            }
            n--;
            i--;
        }
    }
    
    std::ofstream out("output2.txt");
    if(!out.is_open())
    {
        std::cerr<<"File error"<<std::endl;
    }
    for(int i = 0; i < n; i++)
    {
        out << new_words[i] << std::endl;
    }
}


int main()
{
    int n;
    std::string new_words[N_MAX];
    std::string words[N_MAX];
    if (!(Read (n, words)))
        return -1;
    if (isPalindrome (n,words))
    {
        part_vowels(n, words);
        write1(n, words);
    }
    else
    {
        delete_vowels_double_consonants(n, words, new_words);
        write2(n,new_words);
    }
    return 0;
}



