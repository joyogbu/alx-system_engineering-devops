#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
int main(void)
{
	int i = 0;
	pid_t c_pid;
	while (i < 5)
	{
		c_pid = fork();
		if (c_pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", c_pid);
		}
		i++;
	}
	infinite_while;
	return (0);;
}

