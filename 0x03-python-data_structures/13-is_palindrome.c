#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 0 if it is not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *tmp;
	int *array, list_len = 0, idx = 0;

	if (!head || !*head || !(*head)->next)
		return (1);
	current = tmp = *head;
	while (tmp)
	{
		tmp = tmp->next;
		list_len++;
	}

	array = malloc(sizeof(int) * list_len);
	if (!array)
		exit(1);
	for (list_len = 0; current; list_len++)
	{
		array[list_len] = current->n;
		current = current->next;
	}
	list_len--;

	while (idx < list_len)
	{
		if (array[idx++] != array[list_len--])
		{
			free(array);
			return (0);
		}
	}
	free(array);

	return (1);
}
