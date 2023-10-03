#include "lists.h"

/**
 * insert_node - inserts node
 * @head: list head
 * @number: index where the new node is located
 * Return: the address of new node, NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *jadid;
	listint_t *rass;
	listint_t *prv_rass;

	rass = *head;
	jadid = malloc(sizeof(listint_t));

	if (jadid == NULL)
		return (NULL);

	while (rass != NULL)
	{
		if (rass->n > number)
			break;
		prv_rass = rass;
		rass = rass->next;
	}

	jadid->n = number;

	if (*head == NULL)
	{
		jadid->next = NULL;
		*head = jadid;
	}
	else
	{
		jadid->next = rass;
		if (rass == *head)
			*head = jadid;
		else
			prv_rass->next = jadid;
	}

	return (jadid);
}
