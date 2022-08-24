#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to the head of the list
 * @number: number to be inserted
 *
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;
	listint_t *previous;

	current = *head;
	if (current == NULL)
		return (add_nodeint_end(head, number));
	while (current->n <= number)
	{
		if (current->next == NULL)
			return (add_nodeint_end(head, number));
		previous = current;
		current = current->next;
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = current->next;
	previous->next = new;

	return (new);
}
