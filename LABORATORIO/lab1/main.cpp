#include <iostream>
#include "BMP.h"
#include <iostream>
#include <cstring>

int main(int argc, char *argv[]) {
	BMP bmp1(argv[1]);
	std::string copy;
	 copy=argv[1];
	 bmp1.write("_copy.bmp");
	 int size=bmp1.data.size();
	 std::cout << size << '\n';
	 for (size_t i = 0; i < size/2; i+=3) {
	 		//bmp1.data[i]+=2;
			bmp1.data[i+1]+=2;
			bmp1.data[i+2]-=11;
	 }
	 bmp1.write("_copy_modificada.bmp");

}
