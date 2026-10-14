#include <string>

inline std::string greet(const std::string& name = "")
{
    if (!name.empty()) {
        return "Hello " + name;
    }
    return "Hello";
}

inline int add(int a, int b)
{
    return a + b;
}
