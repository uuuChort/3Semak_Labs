#include <iostream>
#include "Tree.h"
#include <string>
#include <vector>


using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
	vector <int> dV, cV, rV, rdV, rcV, rrV;
	string str = "8(3(1,6(4,7)),10(,14(13,)))";
	tree::Tree tree;
	tree = tree.parse(str);
	tree.Print();

	cout << endl << "Рекурсивные обходы\n";
	Recur_direct(rdV, &tree);
	Recur_center(rcV, &tree);
	Recur_reverse(rrV, &tree);

	direct(dV, &tree);
	center(cV, &tree);
	reverse(rV, &tree);


	for (auto& value : rdV)
	{
		cout << value << "\t";
	}
	cout << endl;
	for (auto& value : rcV)
	{
		cout << value << "\t";
	}
	cout << endl;
	for (auto& value : rrV)
	{
		cout << value << "\t";
	}

	cout << endl << "Не рекурсивные обходы\n";

	for (auto& value : dV)
	{
		cout << value << "\t";
	}
	cout << endl;
	for (auto& value : cV)
	{
		cout << value << "\t";
	}
	cout << endl;
	for (auto& value : rV)
	{
		cout << value << "\t";
	}
}