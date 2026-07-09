#include <SFML/Graphics.hpp>
#include <vector>
#include <iostream>

const int window_w = 1280;
const int window_h = 720;
const int player_r = 20.f;
const int collectable_r = 10.f;
const int num = 30;

class Collect {
    public:
        sf::CircleShape ball;
        Collect(int x, int y){
            ball.setRadius(collectable_r);
            ball.setFillColor(sf::Color::Red);
            ball.setPosition(x, y);
            ball.setOrigin(collectable_r / 2, collectable_r / 2);
        }
};

bool Collision(const sf::CircleShape& circle1, const sf::CircleShape& circle2) {
    sf::Vector2f center1 = circle1.getPosition();
    sf::Vector2f center2 = circle2.getPosition();
    float Sum = circle1.getRadius() + circle2.getRadius();

    float distanceX = center1.x - center2.x;
    float distanceY = center1.y - center2.y;
    float squaredDistance = distanceX * distanceX + distanceY * distanceY;

    return squaredDistance <= Sum * Sum;
}


int main()
{
    sf::RenderWindow window(sf::VideoMode(window_w, window_h), "SFML works!");
    sf::CircleShape shape(player_r);
    shape.setFillColor(sf::Color::Green);
    shape.setPosition(window_w / 2, window_h / 2);
    shape.setOrigin(player_r, player_r);

    std::vector<Collect> collectibles;
    for (int i = 0; i < num; i++) {
        float x = rand() % (window_w - 2 * collectable_r) + collectable_r;
        float y = rand() % (window_h - 2 * collectable_r) + collectable_r;
        collectibles.emplace_back(x, y);
    }
    int cnt = 0;

    sf::Clock clock;

    sf::Font font;
    if (!font.loadFromFile("fonts/arial.ttf")){
        std::cerr << "Error loading font." << std::endl;
        return EXIT_FAILURE;
    }

    sf::Text text;
    text.setFont(font);
    text.setCharacterSize(14);
    text.setFillColor(sf::Color::White);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        const float speed = 0.5;
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) {
            if (shape.getPosition().x > player_r) {
                shape.move(-speed, 0);
            }
        } else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) {
            if (shape.getPosition().x < window_w - player_r) {
                shape.move(speed, 0);
            }
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
            if (shape.getPosition().y > player_r) {
                shape.move(0, -speed);
            }
        } else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
            if (shape.getPosition().y < window_h - player_r) {
                shape.move(0, speed);
            }
        }

        for (auto i = collectibles.begin(); i != collectibles.end();) {
            if (Collision(shape, i->ball)){
                i = collectibles.erase(i);
                cnt++; 
            }
             else
                ++i;
        }
        

        
        
        std::string message = "Collected: " + std::to_string(cnt) +
                             "\nTime: " + std::to_string(clock.getElapsedTime().asSeconds());
        text.setString(message);
        text.setPosition(10, 10);

        if (cnt == num) {
            cnt++;
            text.setString("You won. Time taken: " + std::to_string(clock.getElapsedTime().asSeconds()));
            text.setPosition(window_w / 2, window_h / 2);
            window.draw(text);
            window.display();
        } else if (cnt < num){
            window.clear(sf::Color::Black);
            window.draw(shape);
            for (const auto& collectible : collectibles) {
                window.draw(collectible.ball);
            }
            window.draw(text);
            window.display();
        }
        
    }
    return 0;
}