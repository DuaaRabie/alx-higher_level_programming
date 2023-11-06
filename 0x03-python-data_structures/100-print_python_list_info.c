#include <Python.h>

/**
 * print_python_list_info - prints python info
 * @p: python object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i = 0, size = Py_SIZE(p);
	int alloc = ((PyListObject *) p)->allocated;
	PyObject *item;

	printf("[*] Size of the Python List = %d\n[*] Allocated = %d\n", size, alloc);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
