#include <iostream>
using namespace std;

int main()
{
	int num, i = 0, binary[32];
	cout << "ondalik - ikilik taban donusumu yapmak istediginiz sayiyi giriniz: ";
	cin >> num;

	while (num > 0)
	{
		binary[i] = num % 2;
		num /= 2;
		i++;
	}

	for (int j = i - 1; j >= 0; j--)
	{
		cout << binary[j];
	}

	return 0;
}