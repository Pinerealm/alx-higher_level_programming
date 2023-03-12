#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 0 if it is not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *array, len_list = 0, idx = 0;

	if (!head || !*head || !(*head)->next)
		return (1);
	current = *head;
	while (current)
	{
		current = current->next;
		len_list++;
	}

	array = malloc(sizeof(int) * len_list);
	while (!array)
		array = malloc(sizeof(int) * len_list);
	current = *head;
	for (len_list = 0; current; len_list++)
	{
		array[len_list] = current->n;
		current = current->next;
	}
	len_list--;

	while (idx < len_list)
	{
		if (array[idx++] != array[len_list--])
		{
			free(array);
			return (0);
		}
	}
	free(array);

	return (1);
}
