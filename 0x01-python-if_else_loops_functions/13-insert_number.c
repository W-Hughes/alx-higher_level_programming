#include "lists.h"
/**
 *insert_node - Inserts a number into a sorted singly linked list.
 *@head: double point to the list
 *@number: The numebr to  insert
 *
 * Return: The address of the new node, otherwise NULL on failure.
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (temp == NULL || temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}

	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
