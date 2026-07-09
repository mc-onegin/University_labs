#include <iostream>
#include <string>
#include <fstream>
#include <set>

const int N_MAX = 2000;

bool Read (int& n, std::string words[N_MAX])
{
    std::ifstream in("input3.txt");
    if (!in.is_open())
    {
        std::cerr<<"File error"<<std::endl;
        return false;
    }
    n=0;
    while (!in.eof())
    {
        in>> words[n];
        n++;
    }

    return true;
}

bool serch_7_letters(std::string word, std::string& unique)
{   
    int count=0;
    unique.clear();
    //std::set<char> unique_char;
    std::string mas;
    for (char c : word)  
        if (std::isalpha(c) && (mas.find(c)==std::string::npos))
        {
            //unique_char.insert(c);
            mas+=c;
            unique+=c;
            count++;
        }
    //return unique_char.size() > 7;
    return count > 7;
}

void upper_letters(int n, std::string words[N_MAX], std::string unique[N_MAX])
{
    for (int i=0; i<n; i++)
        if (serch_7_letters(words[i], unique[i]))
            for (int j=0; j<words[i].length();j++)
                words[i][j]=toupper(words[i][j]);
        else 
        {
            unique[i].clear();
        }
}

void write(int n,std::string words[N_MAX],std::string unique[N_MAX])
{
    std::ofstream out("output3.txt");
    if(!out.is_open())
    {
        std::cerr<<"File error"<<std::endl;
    }
    for (int i=0; i<n; i++)
    {   
        if(!unique[i].empty())
            out << words[i] << "("<<unique[i]<<")"<<" ";
        else
            out<< words[i]<<" ";
    }
}     


int main ()
{
    int n;
    std::string unique[N_MAX];
    std::string words[N_MAX];
    if (!(Read (n, words)))
        return -1;
    upper_letters(n,words,unique);
    write(n, words, unique);

    return 0;
}