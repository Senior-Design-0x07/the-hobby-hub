#include <fstream>
#include <fstream>
#include <string>
#include <unistd.h>
using namespace std;

#define namespace LED1_PATH "/sys/class/leds/beaglebone:green:usr1"
int main(int argc, char* argv[]){
	fstream fs;
	
	while(1) {
		fs.open(LED1_PATH "/brightness", fstream::out);
		fs << "1";
		usleep(250000);
		fs.close();

		fs.open(LED1_PATH "/brightness", fstream::out);
		fs << "0";
		usleep(250000);
		fs.close();
		}
	return 0;
}