#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode(640, 480), "SFML is open");

    sf::Texture texture;
    if (!texture.loadFromFile("sfml.PNG"))
    {
        return EXIT_FAILURE;
    }

    sf::CircleShape triangle(40.f, 3);
    triangle.setPosition(500, 200);
    triangle.setFillColor(sf::Color::Blue);
    triangle.rotate(45);

    sf::CircleShape shape(1.f);
    shape.setFillColor(sf::Color::Yellow);
    shape.setTexture(&texture);

    sf::RectangleShape rectangle(sf::Vector2f(200, 100));
    rectangle.setFillColor(sf::Color(100, 100, 200));
    rectangle.setOutlineThickness(2);
    rectangle.setOutlineColor(sf::Color::White);
    rectangle.setPosition(150, 200);
    rectangle.rotate(60);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Right)){
            shape.setRadius(80.f);
            shape.move(1.33f, 1.f);
        }

        window.clear(sf::Color(255, 0, 0));
        window.draw(shape);
        window.draw(triangle);
        window.draw(rectangle);
        window.display();
    }

    return 0;
}