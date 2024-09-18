#include "lists.h"

/**
 *is_palindrome - checks if a list is palindrome
 *@head: Double pointer to the head.
 *Return: 1 on success, otherwise 0
 */

listint_t *reverse_list(listint_t *head);

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *first_half, *second_half;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverse_list(slow);
	first_half = *head;

	listint_t *second_half_cpy = second_half;

	while (second_half)
	{
		if (first_half->n != second_half->n)
		{
			reverse_list(second_half_cpy);
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	reverse_list(second_half_cpy);
	return (1);

}

/**
 *reverse_list - Reverses a linked list;
 *@head: pointer to the head of the list
 *Return: Pointer to the new head
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
