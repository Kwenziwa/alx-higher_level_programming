/*
 * File: 103-python.c
 */

#include <Python.h>

void print_python_list(PyObject *pyobj);
void print_python_bytes(PyObject *pyobj);

/**
 * print_python_list - Prints basic info about Python lists.
 * @pyobj: A PyObject list object.
 */
void print_python_list(PyObject *pyobj)
{
	int aszi, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)pyobj;
	PyVarObject *var = (PyVarObject *)pyobj;

	aszi = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", aszi);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < aszi; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @pyobj: A PyObject byte object.
 */
void print_python_bytes(PyObject *pyobj)
{
	unsigned char i, aszi;
	PyBytesObject *bytes = (PyBytesObject *)pyobj;

	printf("[.] bytes object info\n");
	if (strcmp(pyobj->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  aszi: %ld\n", ((PyVarObject *)pyobj)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)pyobj)->ob_size > 10)
		aszi = 10;
	else
		aszi = ((PyVarObject *)pyobj)->ob_size + 1;

	printf("  first %d bytes: ", aszi);
	for (i = 0; i < aszi; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (aszi - 1))
			printf("\n");
		else
			printf(" ");
	}
}
