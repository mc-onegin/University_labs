#include <SFML/Graphics.hpp>
#include <string>
#include <iostream>

class Game //класс игрового окна
{
    private:
        unsigned int m_width;
        unsigned int m_height;
        std::string m_title;
        sf::RenderWindow m_window;

        sf::Sprite m_background;//переменные беграунда
        sf::Texture m_backgroundTexture;

        sf::Texture m_end1Texture;
        sf::Sprite m_end1;
        sf::Texture m_end2Texture;
        sf::Sprite m_end2;
        sf::Texture m_end3Texture;
        sf::Sprite m_end3;

        sf::Sprite m_field;//переменные поля
        sf::Texture m_fieldTexture;
        sf::Sprite m_purple;
        sf::Texture m_purpleTexture;
        sf::Sprite m_blue;
        sf::Texture m_blueTexture;
        sf::Sprite m_block;
        sf::Texture m_blockTexture;
        sf::Sprite m_line;
        sf::Texture m_lineTexture;
        float StepPosition[36][3];
        int i_stepP=0;
        int current_frame=1;
        float t_field1;
        float t_field2=0.0;
        void FieldAnimation()
        {
            if(t_field1-t_field2 >=0.5){
                t_field2+=0.5;
                current_frame++;
                switch(current_frame)
                {
                    case 1: m_fieldTexture.loadFromFile("images/field/wind_an0000.png");
                        break;
                    case 2: m_fieldTexture.loadFromFile("images/field/wind_an0001.png");
                        break;
                    case 3: m_fieldTexture.loadFromFile("images/field/wind_an0002.png");
                        break;
                    case 4: m_fieldTexture.loadFromFile("images/field/wind_an0003.png");
                        break;
                    case 5: m_fieldTexture.loadFromFile("images/field/wind_an0004.png");
                        break;
                    case 6: m_fieldTexture.loadFromFile("images/field/wind_an0005.png");
                        break;
                    case 7: m_fieldTexture.loadFromFile("images/field/wind_an0006.png");
                        break;
                    case 8: m_fieldTexture.loadFromFile("images/field/wind_an0007.png");
                        break;
                    case 9: m_fieldTexture.loadFromFile("images/field/wind_an0008.png");
                        break;
                    case 10: m_fieldTexture.loadFromFile("images/field/wind_an0009.png");
                        break;
                    case 11: m_fieldTexture.loadFromFile("images/field/wind_an0010.png");
                        break;
                    default: {   
                        current_frame=1;
                        m_fieldTexture.loadFromFile("images/field/wind_an0000.png");
                        break;
                    }
                }
            }
        }

        int table[6][6];//переменные матрицы поля
        bool Mouse_pressed = true;
        bool First_time=true;
        int count_blue;
        int count_purple;
        int i_y, j_x;
        int score=0;
        int player=1;
        void SetStepPosition()
        {
            StepPosition[i_stepP][0]=sf::Mouse::getPosition(m_window).x;
            StepPosition[i_stepP][1]=sf::Mouse::getPosition(m_window).y;
            StepPosition[i_stepP][2]=table[i_y][j_x];
            i_stepP++;
        }
        void MousePressedOnField(int& player)
        {
            if(score>=36)
                return;
            if(player==1)
                m_line.setPosition(70, 260);
            else
                m_line.setPosition(855, 260);
            if(sf::Mouse::isButtonPressed(sf::Mouse::Left) || sf::Mouse::isButtonPressed(sf::Mouse::Right)){
                if(!Mouse_pressed){
                    //std::cerr << "x: " << sf::Mouse::getPosition(m_window).x << " " << "y: " << sf::Mouse::getPosition(m_window).y << std::endl;
                    j_x=(sf::Mouse::getPosition(m_window).x)/100-2;
                    if(j_x<0 || j_x>5){
                        Mouse_pressed=true;
                        return;
                    }
                    i_y=(sf::Mouse::getPosition(m_window).y);
                    if(i_y>=80 && i_y<=175)
                        i_y=0;
                    else if(i_y>175 && i_y<=260)
                        i_y=1;
                    else if(i_y>260 && i_y<=355)
                        i_y=2;
                    else if(i_y>355 && i_y<=445)
                        i_y=3;
                    else if(i_y>445 && i_y<=535)
                        i_y=4;
                    else if(i_y>535 && i_y<=630)
                        i_y=5;
                    else{
                        Mouse_pressed=true;
                        return;
                    }
                    if(sf::Mouse::isButtonPressed(sf::Mouse::Left)){
                        if(First_time){
                            if(table[i_y][j_x]==0){
                                score++;
                                table[i_y][j_x]=player;
                                SetStepPosition();
                                switch (player)
                                {
                                case 1: m_purple.setPosition(sf::Mouse::getPosition(m_window).x, sf::Mouse::getPosition(m_window).y);
                                    count_purple++;
                                    break;
                                case 2: m_blue.setPosition(sf::Mouse::getPosition(m_window).x, sf::Mouse::getPosition(m_window).y);
                                    count_blue++;
                                    break;
                                default:
                                    break;
                                }
                                /*for(int i=0; i<6; i++){
                                    for(int j=0; j<6; j++)
                                        std::cerr << table[i][j] << " ";
                                    std::cerr << std::endl;}*/
                                player++;
                                if(player==3){
                                    First_time=false;
                                    player=1;
                                    Mouse_pressed=true;
                                }
                                MousePressedOnField(player);
                                return;
                            }
                        }

                        if(table[i_y][j_x]==0 && ((table[i_y-1][j_x]==player && i_y-1>=0) || (table[i_y+1][j_x]==player && i_y+1<=5) 
                            || (table[i_y][j_x-1]==player && j_x-1>=0) || (table[i_y][j_x+1]==player && j_x+1<=5))){
                            score++;
                            table[i_y][j_x]=player;
                            SetStepPosition();
                            switch (player)
                            {
                                case 1: m_purple.setPosition(sf::Mouse::getPosition(m_window).x, sf::Mouse::getPosition(m_window).y);
                                    count_purple++;
                                    break;
                                case 2: m_blue.setPosition(sf::Mouse::getPosition(m_window).x, sf::Mouse::getPosition(m_window).y);
                                    count_blue++;
                                    break;
                                default:
                                    break;
                            }
                            /*for(int i=0; i<6; i++){
                                for(int j=0; j<6; j++)
                                    std::cerr << table[i][j] << " ";
                                std::cerr << std::endl;}*/
                            player++;
                            if(player==3){
                                player=1;
                                Mouse_pressed=true;
                            }
                            MousePressedOnField(player);
                            return;
                        }
                        else{
                            Mouse_pressed=true;
                            return;
                        }
                    }
                    else if(sf::Mouse::isButtonPressed(sf::Mouse::Right) && !First_time){
                        if(table[i_y][j_x]==0){
                            score++;
                            table[i_y][j_x]=-1;
                            StepPosition[i_stepP][0]=(j_x + 2)*100+5;
                            switch(i_y)
                            {
                                case 0: StepPosition[i_stepP][1]=80;
                                    break;
                                case 1: StepPosition[i_stepP][1]=170;
                                    break;
                                case 2: StepPosition[i_stepP][1]=260;
                                    break;
                                case 3: StepPosition[i_stepP][1]=350;
                                    break;
                                case 4: StepPosition[i_stepP][1]=440;
                                    break;
                                case 5: StepPosition[i_stepP][1]=530;
                                    break;
                                default: break;
                            }
                            //std::cerr << "x2: " << j_x*100 << " y2: " << i_y*100-60 << std::endl;
                            StepPosition[i_stepP][2]=table[i_y][j_x];
                            i_stepP++;
                            /*for(int i=0; i<6; i++){
                                for(int j=0; j<6; j++)
                                    std::cerr << table[i][j] << " ";
                                std::cerr << std::endl;}*/
                            player++;
                            if(player==3){
                                player=1;
                                Mouse_pressed=true;
                            }
                            MousePressedOnField(player);
                            return;
                        }
                        else{
                            Mouse_pressed=true;
                            return;
                        }
                    }
                }
            }
            else
                Mouse_pressed=false;
        }

    public:
        Game(unsigned int width, unsigned int height, const std::string& title) //конструктор 
        {
            m_width = width;
            m_height = height;
            m_title = title;
            for(int i=0; i<6; i++)
                for(int j=0; j<6; j++)
                    table[i][j]=0;
            for(int i=0; i<36; i++)
                for(int j=0; j<3; j++)
                    StepPosition[i][j]=0;
        }

        bool Setup()//создание окна
        {
            m_window.create(sf::VideoMode(m_width, m_height), m_title);//создание окна
        
            if(!m_backgroundTexture.loadFromFile("images/window/wind_st.png")) //подгрузка и проверка беграунда
            {
                std::cerr << "Error loading wind_st.png" << __FILE__ << " " << __LINE__ << std::endl;    
                return false;
            }
            m_background.setTexture(m_backgroundTexture);

            m_fieldTexture.loadFromFile("images/field/wind_an0000.png");//подгрузка поля
            m_field.setTexture(m_fieldTexture);

            //std::cerr << 1 << std::endl;

            m_end1Texture.loadFromFile("images/window/end_1.png");//подгрузка поля
            m_end1.setTexture(m_end1Texture);
            m_end2Texture.loadFromFile("images/window/end_2.png");//подгрузка поля
            m_end2.setTexture(m_end2Texture);
            m_end3Texture.loadFromFile("images/window/end_3.png");//подгрузка поля
            m_end3.setTexture(m_end3Texture);

            //std::cerr << 2 << std::endl;

            m_purpleTexture.loadFromFile("images/sprites/purple.png");
            m_purple.setTexture(m_purpleTexture);
            m_purple.setOrigin(49, 45);
            m_purple.setPosition(-100, -100);

            m_blueTexture.loadFromFile("images/sprites/blue.png");
            m_blue.setTexture(m_blueTexture);
            m_blue.setOrigin(49, 45);
            m_blue.setPosition(-100, -100);

            //std::cerr << 6 << std::endl;

            m_blockTexture.loadFromFile("images/sprites/block.png");
            m_block.setTexture(m_blockTexture);
            m_block.setPosition(-100, -100);

            m_lineTexture.loadFromFile("images/sprites/line.png");
            m_line.setTexture(m_lineTexture);

            return true;
        }

        void LifeCycle()
        {
            sf::Clock clock;
            
            while (m_window.isOpen())//события в самой игре пока открыто окно
            {
                sf::Event event;//обработка закрытия окна
                while (m_window.pollEvent(event)) {
                    if (event.type == sf::Event::Closed)
                        m_window.close();
                }

                t_field1=clock.getElapsedTime().asSeconds();//смена кадров поля (анимация)
                FieldAnimation();

                MousePressedOnField(player);
  
                m_window.clear();
                if(score<36){
                m_window.draw(m_background);//отрисовка беграунда
                m_window.draw(m_field);//отрисовка поля
                m_window.draw(m_line);
                    for(int i=0; i<=i_stepP; i++){
                        if(StepPosition[i][2]==1){
                            m_purple.setPosition(StepPosition[i][0], StepPosition[i][1]);
                            m_window.draw(m_purple);
                        }
                        else if(StepPosition[i][2]==2){
                            m_blue.setPosition(StepPosition[i][0], StepPosition[i][1]);
                            m_window.draw(m_blue);
                        }
                        else if(StepPosition[i][2]==-1){
                            m_block.setPosition(StepPosition[i][0], StepPosition[i][1]);
                            m_window.draw(m_block);
                        }
                    }
                }
                else if(score==36){
                    if(count_blue == count_purple)
                        m_window.draw(m_end3);
                    else if(count_blue > count_purple)
                        m_window.draw(m_end2);
                    else
                        m_window.draw(m_end1);
                }
                m_window.display();
            }
        }

};

int main()
{
    Game game(979, 730, "Points");
    if(!game.Setup()) {
        std::cerr << "Error" << std::endl;
        return -1;
    }
    game.LifeCycle();
    return 0;
}