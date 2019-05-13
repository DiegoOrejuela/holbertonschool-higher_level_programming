#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: object type list.
 *
 * Return: nothing.
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size_list = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Size of the Python List = %lu\n", size_list);
	printf("[*] Allocated = %lu\n", (*list).allocated);

	for (i = 0; i < size_list; i++)
	{
		printf("Element %lu: %s\n", i, (*Py_TYPE((*list).ob_item[i])).tp_name);
	}
}
