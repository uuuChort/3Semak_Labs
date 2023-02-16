#include <iostream>


using namespace std;

int main()
{
	unsigned long long int k;
	cin >> k;
	unsigned long long int g = k, a = 1, b = 1, c = 1;
	//Максимальное степень числа
	while (g >= 3) {
		a = a + 1;
		g = g / 3;
	}
	g = k;
	while (g >= 5) {
		b = b + 1;
		g = g / 5;
	}
	g = k;
	while (g >= 7) {
		c = c + 1;
		g = g / 7;
	}
	
	//перебор
	double ss;
	for (int i = 0; i <= a; i++) {
		for (int j = 0; j <= b; j++) {
			for (int p = 0; p <= c; p++) {
				ss = pow(3, i) * pow(5, j) * pow(7, p);
				if (ss <= k) {
					std::cout << ss << "; ";
				}
			}
		}
	}
}



