#include <Python.h>
#include <stdio.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p);

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
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", size_list);
	printf("[*] Allocated = %lu\n", (*list).allocated);

	for (i = 0; i < size_list; i++)
	{
		type = (*(*(*list).ob_item[i]).ob_type).tp_name;
		printf("Element %lu: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes((*list).ob_item[i]);
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
	size_t length;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %lu\n", PyBytes_Size(p));
	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	if (strlen(str) >= 9)
		length = 10;
	else
		length = strlen(str) + 1;
	printf("  first %lu bytes:", length);
	for (i = 0; str[i] != '\0' && i < 10; i++)
	{
		printf(" %02x", str[i]);
	}
	if (strlen(str) <= 9)
		printf(" %02x", str[i]);

	printf("\n");
}
