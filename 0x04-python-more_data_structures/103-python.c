#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints python bytes
 * @p: python object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *firstbytes;
	Py_ssize_t size;
	int i;

	if (!(PyBytes_Check(p)))
		printf("[ERROR] Invalid Bytes Object");
	else
	{
		(int)(PyBytes_AsStringAndSize(p, &firstbytes, &size));
		printf("[.] bytes object info\n");
		printf("  size: %d\n", (int)(PyBytes_Size(p)));
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first %d bytes:", (int)size < 10? (int)size + 1 : 10);
		for (i = 0; i <= size && i < 10; i++)
		{
			printf("%02x", (unsigned char)*firstbytes);
			printf("%s", i == size || i == 9 ? "\n" : " ");
			firstbytes++;
		}
	}
	
}
