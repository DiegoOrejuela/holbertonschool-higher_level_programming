#include <Python.h>
#include <stdio.h>
#include <bytesobject.h>

/**
 * print_python_list - prints some basic info about Python lists.
 * @p: object type list.
 *
 * Return: nothing.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size_list = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", size_list);
	printf("[*] Allocated = %lu\n", (*list).allocated);

	for (i = 0; i < size_list; i++)
	{
		printf("Element %lu: %s\n", i, (*Py_TYPE((*list).ob_item[i])).tp_name);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: object type list.
 *
 * Return: nothing.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	int i;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %lu\n", PyBytes_Size(p));
	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	printf("  first %lu bytes:", strlen(str));
	for (i = 0; str[i] != '\0' && i < 10; i++)
	{
		printf(" %02x", str[i]);
	}
	printf("\n");
}
