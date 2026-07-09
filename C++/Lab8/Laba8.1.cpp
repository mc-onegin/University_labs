#include <iostream>
#include <string>
#include <fstream>
#include <set>
const int N_MAX = 2000;

bool Read (int& n, int& cnt, std::string words[N_MAX]) 
{
    std::ifstream in("input1.txt");
    if (!in.is_open())
    {
        std::cerr<<"File error"<<std::endl;
        return false;
    }
    in>>n;
    cnt=0; 
    while (!in.eof())
    {
        in>> words[cnt];
        for(int j = 0; j < words[cnt].length(); j++)
        {
            if(ispunct(words[cnt][j]))
            {
                words[cnt].erase(j, 1);
                j--;
            }
        }
        cnt++;
    }
    return true;
}
bool Write (int& n, int& k, std::string words[N_MAX])
{
    std::ofstream out("output1.txt");
    if(!out.is_open())
    {
        std::cerr<<"File error"<<std::endl;
        return false;
    }
    int count = std::min(n, k);
    for(int i = 0; i < count; i++)
    {
        out << words[i] << std::endl;
    }
    return true;
}

void Sort(int cnt, std::string words[N_MAX])
{
    for (int i=0; i<cnt;++i)
        for (int j=0; j<cnt; ++j)
            if ((words[i].length()>words[j].length()) || ((words[i].length()==words[j].length())
             && (tolower(words[i][0])>(tolower(words[j][0])))))
                std::swap(words[i], words[j]); 
}

void ConsonantsInOrder(int cnt, int& k, std::string words[N_MAX], std::string new_words[N_MAX])
{  
    for (int i = 0; i < cnt; i++)
    {    
        char prev_consonant = 'a';
        bool flag = false;
        for (int j = 0; j < words[i].length(); j++)
        {
            words[i][j] = tolower(words[i][j]);
            if (!(words[i][j] == 'a' || words[i][j] == 'e' || words[i][j] == 'i' || words[i][j] == 'o' || words[i][j] == 'u' || words[i][j] == 'y'))
            {
                flag = true;
                if (prev_consonant > words[i][j])
                {
                    flag = false;
                    break;
                }
                prev_consonant = words[i][j];
            }
        }
        if(flag)
        {
            new_words[k] = words[i];
            k++;      
        }
    }
}

int main ()
{
    int n, cnt, k=0;
    std::string words[N_MAX];
    std::string new_words[N_MAX];
    if (!(Read (n, cnt, words)))
        return -1;    
    ConsonantsInOrder(cnt, k, words, new_words);
    Sort(k, new_words);
    for(int i = 0; i < k; i++)
    {
        if(new_words[i] == new_words[i+1])
        {
            for(int j = i; j < k; j++)
            {
                new_words[j] = new_words[j + 1];
            }
            k--;
        }
    }
    Write(k, n, new_words);

    return 0;
}