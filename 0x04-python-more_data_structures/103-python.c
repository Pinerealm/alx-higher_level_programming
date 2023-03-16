#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <assert.h>
#include <pyport.h>
#include <object.h>
#include <bytesobject.h>
#include <listobject.h>
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyObject *item;
	Py_ssize_t len, idx;

	len = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (idx = 0; idx < len; idx++)
	{
		item = list->ob_item[idx];
		printf("Element %ld: %s\n", idx, item->ob_type->tp_name);
		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[idx]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_len, idx;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));

	bytes_len = PyBytes_Size(p) < 10 ? PyBytes_Size(p) + 1 : 10;
	printf("  first %ld bytes: ", bytes_len);
	for (idx = 0; idx < bytes_len; idx++)
		printf("%02hhx ", PyBytes_AsString(p)[idx]);
	printf("\n");
}
