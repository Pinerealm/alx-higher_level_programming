#include "lists.h"
listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 0 if it is not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *top, *bottom;

	if (!head || !(*head) || !(*head)->next)
		return (1);
	top = *head;
	bottom = reverse_listint(head);

	while (top && bottom)
	{
		if (top->n != bottom->n)
			return (0);
		top = top->next;
		bottom = bottom->next;
	}

	return (1);
}

/**
 * reverse_listint - reverses a listint_t singly-linked list
 * @head: double pointer to head of the list
 *
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;

	if (!head || !(*head))
		return (NULL);
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;

	return (*head);
}
