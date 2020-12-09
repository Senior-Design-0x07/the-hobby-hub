#include <fstream>
#include <fstream>
#include <string>
#include <unistd.h>
using namespace std;

#define LED0_PATH "/sys/class/leds/beaglebone:green:usr0"

int main(int argc, char* argv[]){
	fstream fs;
	
	while(1) {
		fs.open(LED0_PATH "/brightness", fstream::out);
		fs << "1";
		usleep(500000);
		fs.close();

		fs.open(LED0_PATH "/brightness", fstream::out);
		fs << "0";
		usleep(500000);
		fs.close();
		}
	return 0;
}
