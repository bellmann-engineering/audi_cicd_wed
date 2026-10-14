#include <gtest/gtest.h>

#include "calc.hpp"

TEST(GreetTest, OhneName)
{
    //         real   erwartung
    EXPECT_EQ(greet(), "Hello");
}

TEST(GreetTest, MitName)
{
    EXPECT_EQ(greet("Kai"), "Hello Kai");
}

TEST(AddTest, Positiv)
{
    EXPECT_EQ(add(2, 3), 5);
}

TEST(AddTest, Negativ)
{
    EXPECT_EQ(add(-1, 1), 0);
}
