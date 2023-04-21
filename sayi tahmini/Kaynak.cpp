#include <iostream>
#include <cstdlib>

using namespace std;

int sayi_tahmin(int);

int main()
{
	int num;
	cout << "tuttugum sayiyi tahmin et: ";
	cin >> num;
	sayi_tahmin(num);

	return 0;
}

int sayi_tahmin(int x)
{
	srand((unsigned)time(NULL));
	int random = rand() % 1000;
	int i = 1;

	while (i < 8)
	{
		i++;
		if (x > random)
		{
			cout << x << " tuttugum sayidan daha buyuk" << endl << "tekrar dene : ";
			cin >> x;

		}
		else if (x < random)
		{
			cout << x << " tuttugum sayidan daha kucuk" << endl << "tekrar dene : ";
			cin >> x;
		}
		else
		{
			cout << "dogru tahmin" << endl;
			break;
			system("PAUSE");
		}

		if (i == 8)
		{
			cout << "oyun bitti, tuttugum sayi: " << random;
		}
	}
	return 0;
}