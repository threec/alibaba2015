# recored 结果记录

## model0
	常数项，用户最后一天对该物品行为量  logistic回归 
	
	训练集F1=1.16, 测试集F1=2.9 
	加权比1:100， C=0.0077
	
	
	全部数据 F1 = 1.8%
	best score 0.017293583882
	best parms {'C': 0.00021544346900318845, 'class_weight': {0: 1, 1: 100}}
	
	best score 0.0202207657264
	best parms {'C': 0.0001, 'class_weight': {0: 1, 1: 70}}
	
	
	best score 0.0171046056146
	best parms {'C': 0.0021544346900318821, 'class_weight': {0: 1, 1: 200}}
	clf parms: -3.2126734833 1.52233247361

	F1      P       R
	1.60    0.91    6.62

			F       T
	N   4576851     2171
	P       282     20
	
## model1
	常数项，	用户对该物品总行为量，用户最后一天对该物品行为量  logistic回归 
	[-4.57766365] [[ 0.65020026  1.34236491]]
	训练集F1 = 0.94 测试集F1=3.6
	加权比1:100， C=0.0013
	
	利用所有数据，调优发现
	[-2.81781935] [[-0.16534085  1.45092141]]
	F1 = 1.78913738019%
	
	best score 0.016934551864
	best parms {'C': 2.1544346900318823e-05, 'class_weight': {0: 1, 1: 200}}
	clf parms: -1.76501368526 -0.563198009584 1.36522998316

	F1      P       R
	2.02    1.30    4.64

			F       T
	N     4577955   1067 
	P       288     14
	

## model2
	常数项，	用户最后一天行为量，用户最后一天对该分类行为量  logistic回归 
	
	训练集F1 = 1.3， 测试集F1=2.7
	加权比1：100， C=0.046
	
	采用全部数据集后
	[-3.22274269] [[ 1.69565179 -0.21331802]]
	F1 = 2.09%
	加权比1:100，C=0.00021544346900318845
	
	best score 0.0180839420153
	best parms {'C': 0.0021544346900318821, 'class_weight': {0: 1, 1: 200}}
	clf parms: -3.05375335799 1.75200734273 -0.174489993525

	F1      P       R
	1.81    1.02    7.95

			F       T
	N     4576693   2329 
	P       278     24
	
## model3 (和模型2本质相同)
	用户最后一天对物品行为量， 最后一天对该物品/最后一天对该类
	best score 0.0201229461605
	best parms {'C': 0.0001, 'class_weight': {0: 1, 1: 70}}
	
	
	best score 0.0179560337304
	best parms {'C': 0.0021544346900318821, 'class_weight': {0: 1, 1: 200}}
	clf parms: -3.33796542765 1.41771384108 0.73993477003

	F1      P       R
	1.87    1.09    6.62

			F       T
	N   4577204     1818   
	P       282     20

## model4 *
	常数项，	用户最后一天对物品行为量，用户最后一天对该分类行为量，用户转化率 logistic回归 
	
	best score 0.0180369104645
	best parms {'C': 0.0021544346900318821, 'class_weight': {0: 1, 1: 200}}
	clf parms: -3.06113171244 1.7510171625 -0.173875520012 0.697610373863

	F1      P       R
	1.81    1.02    7.95

			F       T
	N    4576690    2332   
	P       278     24
	
## model5
用户最后一天对物品行为量，用户最后一天对该分类行为量，用户转化率，用户总活跃度
	best score 0.0160327716802
	best parms {'C': 0.01, 'class_weight': {0: 1, 1: 200}}
	clf parms: -2.57683509693 1.73799458623 -0.159567672777 3.08319730965 -0.0720672
	891184



	F1      P       R
	1.68    0.95    7.28

			F       T
	N     4576727   2295 
	P       280     22
	
	用户总活跃度没用
	
## model6
用户最后一天对物品行为量，用户最后一天对该分类行为量，用户转化率，商品最后一天热门程度

	best score 0.0181142780741
	best parms {'C': 0.0021544346900318821, 'class_weight': {0: 1, 1: 200}}
	clf parms: -3.04832973967 1.81527178225 -0.174940600552 0.698102032411 -0.065003
	5007965

	F1      P       R
	1.81    1.02    7.95

			F       T
	N    4576702    2320
	P       278     24
	
	商品最后一天热门程度 没有用
	
	将最后一天热门程度改为商品转化率 还是没用
	
	best score 0.0169921514151
	best parms {'C': 0.0021544346900318821, 'class_weight': {0: 1, 1: 200}}
	clf parms: -3.06885170525 1.7466379079 -0.171969799941 0.692126806302 0.849719897682

	F1      P       R
	1.70    0.96    7.62

			F       T
	N       4576638	2384    
	P       279     23
	
## mode7
	特征
	2 user_action_count
	3 user_lastday_count
	4 user_buy_count
	5 item_click_count
	6 item_lastday_count
	7 item_buy_count
	8 cat_click_count
	9 cat_buy_count
	10 user_cat_count
	11 user_cat_lastday_count
	12 user_item_count
	13 user_item_lastday_count
	14 user_add_car
	15 user_add_star
	16 item_added_car
	17 item_added_start
	18 user_item_lasttime


	best score 0.598093712254
	best parms {'C': 1.0}
	clf parms: 0.0 -0.503680755658 -0.0261157564643 0.389699200489 -0.570991174428 0
	.0 -0.199626042298 -0.589764951336 0.700835369893 -0.391130392824 0.177812604406
	 1.63355388487 1.12416907038 0.00315413046176 0.11178421992 1.01544624208 0.0349
	256663566 0.168475029007

	F1      P       R
	60.40   76.26   50.00

			F       T
	N       47      4557
	P       151     151
	
	采样参数控制在0.02左右
	
	best score 0.130854419874
	best parms {'C': 0.69519279617756058}
	clf parms:
	intercept	0.000000
	user_action_count	-0.371763
	user_lastday_count	-0.066816
	user_buy_count	0.331509
	item_click_count	-0.502071
	item_lastday_count	-0.002984
	item_buy_count	-0.457847
	cat_click_count	-0.802509
	cat_buy_count	0.858689
	user_cat_count	-0.260454
	user_cat_lastday_count	0.208004
	user_item_count	1.295417
	user_item_lastday_count	1.064782
	user_add_car	0.031094
	user_add_star	0.109781
	item_added_car	1.082721
	item_added_start	0.036579
	user_item_lasttime	0.030474

	F1      P       R
	13.07   46.00   7.62

			F       T
	N       91405   27
	P       279     23


	===== for test =====
			F       T
	N       4577340 1682
	P       279     23
	F1      P       R
	2.29    1.35    7.62

## model8 
在7的基础上增加了转化率

	best score 0.135714752904
	best parms {'C': 233.57214690901213}
	clf parms:
	intercept       0.402688
	user_action_count       -0.135196
	user_lastday_count      -0.067643
	user_buy_count  0.121783
	item_click_count        -0.557212
	item_lastday_count      -0.047574
	item_buy_count  -0.289825
	cat_click_count -0.823642
	cat_buy_count   0.888391
	user_cat_count  -0.275224
	user_cat_lastday_count  0.207819
	user_item_count 1.351654
	user_item_lastday_count 1.120657
	user_add_car    0.033034
	user_add_star   0.113090
	item_added_car  1.088700
	item_added_start        0.042085
	user_item_lasttime      -0.041916
	item_convert_rate       -5.019174
	user_convert_rate       20.144411




	F1      P       R
	14.25   51.02   8.28

			F       T
	N       91408   24
	P       277     25


	===== for test =====
			F       T
	N       4577224 1798
	P       277     25

	F1      P       R
	2.35    1.37    8.28

## model9
在模型8上又增加了一些特征
	0 user_id
	1 item_id
	2 user_action_count
	3 user_lastday_count
	4 user_buy_count
	5 item_click_count
	6 item_lastday_count
	7 item_buy_count
	8 cat_click_count
	9 cat_buy_count
	10 user_cat_count
	11 user_cat_lastday_count
	12 user_item_count
	13 user_item_lastday_count
	14 user_add_car
	15 user_add_star
	16 item_added_car
	17 item_added_start
	18 user_item_lasttime
	19 cat_add_car
	20 cat_add_star
	21 user_item_buy
	22 user_item_lastweek_click
	23 user_item_lastweek_star
	24 user_item_lastweek_add_car
	25 user_item_lastweek_buy
	26 user_item_halfmonth_click
	27 user_item_halfmonth_star
	28 user_item_halfmonth_add_car
	29 user_item_halfmonth_buy
	30 user_item_before_halfmonth_click
	31 user_item_before_halfmonth_star
	32 user_item_before_halfmonth_add_car
	33 user_item_before_halfmonth_buy
	34 buy
	
	训练结果是
	
	best score 0.284183097713
	best parms {'C': 26.366508987303554}
	clf parms:
	intercept       3.104222
	user_action_count       -0.207504
	user_lastday_count      -0.076293
	user_buy_count  0.242781
	item_click_count        -0.212786
	item_lastday_count      -0.097783
	item_buy_count  0.344305
	cat_click_count -1.224114
	cat_buy_count   0.609725
	user_cat_count  -0.258504
	user_cat_lastday_count  0.077649
	user_item_count 0.332926
	user_item_lastday_count 0.971126
	user_add_car    -0.113400
	user_add_star   0.097122
	item_added_car  0.045578
	item_added_start        0.116045
	user_item_lasttime      0.166021
	cat_add_car     0.563352
	cat_add_star    0.116039
	user_item_buy   -2.159341
	user_item_lastweek_click        0.686702
	user_item_lastweek_star 0.277676
	user_item_lastweek_add_car      1.697815
	user_item_lastweek_buy  0.094305
	user_item_halfmonth_click       0.250627
	user_item_halfmonth_star        -0.413401
	user_item_halfmonth_add_car     0.000000
	user_item_halfmonth_buy 2.074181
	user_item_before_halfmonth_click        -0.002502
	user_item_before_halfmonth_star -0.073459
	user_item_before_halfmonth_add_car      0.007877
	user_item_before_halfmonth_buy  2.615367
	item_convert_rate       -0.535343
	user_convert_rate       14.319559


	F1      P       R
	28.35   63.95   18.21

			F       T
	N       91401   31
	P       247     55


	===== for test =====
			F       T
	N       4576916 2106
	P       247     55

	F1      P       R
	4.47    2.55    18.21
	
