#include <Python.h>

/**
 * print_python_list_info - prints python info
 * @p: python object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i = 0, size = PyList_Size(p);
	int alloc = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %d\n[*] Allocated = %d", size, alloc)
	for (i = 0; i < Py_SIZE(p); i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name)
	}
}
