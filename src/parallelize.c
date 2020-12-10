#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>


#define EXECV_FAILED 127

void kickoff_programs(const char* program_directory) {
    // Spawn a child to run the program.
    pid_t pid = fork();
    if (pid == 0) { // child process
        static char *argv[] = {"echo","Foo is my name.", NULL};
        execv(program_directory, argv);
        exit(EXECV_FAILED); // only if execv fails
    } else { // pid !=0; parent process
        waitpid(pid, 0, 0); // wait for child to exit
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2 || argc > 2) {
        fprintf(stderr, "Please specify the directory containing programs you'd like to run\n");
        return -1;
    }

    kickoff_programs(argv[1]);

    return 0;
}