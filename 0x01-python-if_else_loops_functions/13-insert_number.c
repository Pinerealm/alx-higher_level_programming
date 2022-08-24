#include "lists.h"

listint_t *add_nodeint(listint_t **head, const int n);

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
	if (current->n >= number)
		return (add_nodeint(head, number));
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
	new->next = current;
	previous->next = new;

	return (new);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 *
 * @head: address to the head pointer of the list
 * @n: integer to be added to the new node
 *
 * Return: address of the new node or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}
