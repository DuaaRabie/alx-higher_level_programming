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
	int firstsize, i;
	Py_ssize_t size;

	if (!(PyBytes_Check(p)))
		printf("[ERROR] Invalid Bytes Object");
	else
	{
		firstsize = (int)(PyBytes_AsStringAndSize(p, &firstbytes, &size));
		printf("[.] bytes object info");
		printf("size: %d", (int)(PyBytes_Size(p)));
		printf("trying string: %s", PyBytes_AsString(p));
		printf("first %d bytes:", firstsize);
		for (i = 0; i < firstsize; i++)
		{
			printf("%p", &firstbytes[i]);
			printf("%s", i == firstsize - 1? "\n" : " ");
		}
	}
	
}
