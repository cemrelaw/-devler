#include <iostream>
#include<algorithm>
using namespace std;

int main()
{
	int a, b, c;
	cout << "3 tane tam sayi giriniz: ";
	cin >> a >> b >>  c;
	int liste[3] = { a, b, c };
	sort(liste, liste + 3);
	cout << "1. en buyuk: " << liste[2] << endl <<
		"2. en buyuk: " << liste[1] << endl <<
		"3. en buyuk: " << liste[0];
	return 0;
}