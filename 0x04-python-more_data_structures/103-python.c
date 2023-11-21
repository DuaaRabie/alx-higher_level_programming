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

	printf("[.] bytes object info\n");
	if (!(PyBytes_Check(p)))
		printf("[ERROR] Invalid Bytes Object\n");
	else
	{
		(int)(PyBytes_AsStringAndSize(p, &firstbytes, &size));
		printf("  size: %d\n", (int)(PyBytes_Size(p)));
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first %d bytes: ", (int)size < 10? (int)size + 1 : 10);
		for (i = 0; i <= size && i < 10; i++)
		{
			printf("%02x", (unsigned char)*firstbytes);
			printf("%s", i == size || i == 9 ? "\n" : " ");
			firstbytes++;
		}
	}
	
}

/**
 * print_python_list_info - prints python info
 * @p: python object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	int i = 0, size = ((PyListObject *)p)->ob_base.ob_size;
	int alloc = ((PyListObject *) p)->allocated;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n[*] Allocated = %d\n", size, alloc);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
}
