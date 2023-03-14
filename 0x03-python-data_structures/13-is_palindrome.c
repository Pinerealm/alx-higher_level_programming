#include "lists.h"
int is_palindrome_helper(listint_t **head, listint_t *tail);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 0 if it is not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head || !(*head)->next)
		return (1);
	return(is_palindrome_helper(head, *head));
}

/**
 * is_palindrome_helper - helper function for is_palindrome
 * @head: double pointer to head of list
 * @tail: pointer to tail of list
 *
 * Return: 0 if it is not a palindrome, otherwise 1
 */
int is_palindrome_helper(listint_t **head, listint_t *tail)
{
	int is_palindrome = 1;

	if (tail->next)
		is_palindrome = is_palindrome_helper(head, tail->next);
	if (is_palindrome && (*head)->n == tail->n)
		*head = (*head)->next;
	else
		is_palindrome = 0;

	return (is_palindrome);
}
