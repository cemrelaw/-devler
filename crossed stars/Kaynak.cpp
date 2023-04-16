#include <iostream>
using namespace std;

int main()
{
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (i % 4 == j % 4 || (i & j) % 4 == 1)
			{
				cout << "* ";
			}
			else
			{
				cout << "- ";
			}
		}
		cout << endl;
	}
	return 0;
}