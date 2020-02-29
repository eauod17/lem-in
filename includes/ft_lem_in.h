/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lem_in.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: del-alj <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/27 12:39:05 by del-alj           #+#    #+#             */
/*   Updated: 2020/02/29 14:28:55 by del-alj          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_LEM_IN_H
# define FT_LEM_IN_H

#include <stdio.h>
# include "../libftprintf/headers/libft.h"
# include "../libftprintf/headers/ft_printf.h"

#define MIN_OF2(a, b) (a < b ? a : b)

typedef struct	s_avl
{
	char            *name;
	int				id;
	t_point			cord;
	int             level;
	int				height;
	int				taken;
	struct	s_avl	*left;
	struct  s_avl	*right;
	struct  s_adj   *adj;
}				t_avl;

typedef struct		s_adj
{
	t_avl			*edge;
	int				cap;
	struct s_adj	*next;
}					t_adj;

typedef struct		s_data
{
	int             x;
	int             y;
	char            *room;
	char			*adj_room;
	char            var;
}					t_data;

typedef struct      s_box
{
	t_avl			*tree;
	t_avl           *start;
	t_avl           *end;
	int				ants_nbr;
}					t_box;

typedef struct	s_path
{
	char			*vert_name;
	int				len;
	struct	s_path	*next;
}				t_path;

typedef struct  s_queue
{
	t_adj	*list;
	t_adj	*front;
	t_adj	*rear;
}				t_queue;

t_avl		*ft_new_node(t_data data);
int			ft_height(t_avl *node);
int			ft_max(int a, int b);
void		ft_add_edge(t_avl **tree, char *r1, char *r2);
void		ft_balance(t_avl **tree, t_data data);
void		ft_error_function(t_avl *tree, char *str);
void		ft_if_start_end(t_avl *node, t_data data, t_box *box);
void		ft_insert_node(t_avl **tree, t_data data, t_box *box);
void		ft_print_tree(t_avl *tree, char c);
int			ft_bfs(t_avl *start, t_avl *end);

long long	ft_atoi_m(char *str);
/*
 ** file : parser.c
 */

int	ft_get_room_info(char *str, int i, t_data *data);
int	ft_check_room(char *str, t_data *data);
int	ft_read_input(t_box *head, char **buff);

/*
 ** file : parser_tools.c
 */

char 	*ft_escap_whitspace(char *str);
void	ft_print_link(t_avl *tree , char c);
void	ft_print_all_paths(t_path **paths, int maxflow);

/*
 ** file : ft_error_function.c
 */

void	ft_free_tree(t_avl *tree);

/*
 **	ft_dfs.c
 */

void	ft_increase_capacity(t_adj *edge, t_avl *v, int flow);
int		dfs(t_avl *u, t_avl *v, int flow);
int		ft_get_the_max_flow(t_box *head);
int		ft_get_path(t_avl *u, t_avl *v, t_path **path);
t_path	**ft_all_paths(t_box *head, int	*maxflow);

#endif
