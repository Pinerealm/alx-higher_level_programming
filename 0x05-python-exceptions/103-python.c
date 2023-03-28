#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include <assert.h>
#include <pyport.h>
#include <object.h>
#include <unicodeobject.h>

#include <floatobject.h>
#include <bytesobject.h>
#include <listobject.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyObject *item;
	PyVarObject *var = (PyVarObject *)p;
	Py_ssize_t len, idx;

	len = var->ob_size;
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (idx = 0; idx < len; idx++)
	{
		item = list->ob_item[idx];
		printf("Element %ld: %s\n", idx, item->ob_type->tp_name);
		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[idx]);
		else if (strcmp(item->ob_type->tp_name, "float") == 0)
			print_python_float(list->ob_item[idx]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t bytes_len, idx;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", bytes->ob_sval);

	bytes_len = PyBytes_Size(p) < 10 ? PyBytes_Size(p) + 1 : 10;
	printf("  first %ld bytes: ", bytes_len);
	for (idx = 0; idx < bytes_len; idx++)
	{
		if (idx % 10)
			printf(" ");
		printf("%02hhx", bytes->ob_sval[idx]);
	}
	printf("\n");
}

/**
 * print_python_float - prints some basic info about Python float objects
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *num = (PyFloatObject *)p;

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	printf("  value: %g\n", num->ob_fval);
	fflush(stdout);
}
