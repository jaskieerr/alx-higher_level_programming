#include "lists.h"
/**
 * palindrome - checks if a singly linked list is a palindrome
 * @l: pointer to a pointer to the head of the linked list
 * @r: pointer to the current node being checked for palindrome
 *
 * Return: 0 if palindrome, 1 if not
 */
int palindrome(listint_t **head, listint_t *current)
{
	int ans;

	if (current != NULL)
	{
		ans = palindrome(head, current->next);

		if (ans != 0)
		{
			ans = (current->node == (*head)->node);
			
			*head = (*head)->next;
			
			return (ans);
		}
		return (0);
	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
