#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <assert.h>
#include <pyport.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t len, idx;

	len = PyList_GET_SIZE(list);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (idx = 0; idx < len; idx++)
		printf("Element %ld: %s\n", idx, Py_TYPE(list->ob_item[idx])->tp_name);
}
