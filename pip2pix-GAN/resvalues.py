from weakref import finalize


history1 = {
    "loss_d": [
        0.6913378238677979,
        0.36599913239479065,
        0.07353980094194412,
        0.039109040051698685,
        0.008466213941574097,
        0.0449676476418972,
        0.010267404839396477,
        0.007046603597700596,
        0.0030023809522390366,
        0.0011468069860711694,
        0.003144441405311227,
        0.0020746246445924044,
        0.06309899687767029,
        0.03345470130443573,
        0.0036913964431732893,
        0.011995215900242329,
        0.00838925875723362,
        0.004501467105001211,
        0.003442231798544526,
        0.00045306480024009943,
        0.00027389981551095843,
        0.0001953454193426296,
        0.0016806358471512794,
        0.005747526418417692,
        0.1173272430896759,
        0.04212135449051857,
        0.019329305738210678,
        0.009391256608068943,
        0.004046739544719458,
        0.0034652533940970898,
        0.001199337188154459,
        0.0034234432969242334,
        0.00773517694324255,
        0.005386278964579105,
        0.004903137218207121,
        0.01720820926129818,
        0.0013867918169125915,
        0.0015468921046704054,
        0.0010127266868948936,
        0.00087784044444561,
        0.0004945858963765204,
        0.0008577366825193167,
        0.000317072233883664,
        0.5256521701812744,
        0.05904819816350937,
        0.021192163228988647,
        0.005236329976469278,
        0.009424319490790367,
        0.006696400232613087,
        0.0029815821908414364,
    ],
    "loss_g": [
        12.041399955749512,
        10.1754150390625,
        9.136880874633789,
        9.778023719787598,
        8.625432968139648,
        8.991907119750977,
        8.528021812438965,
        8.405204772949219,
        7.917259216308594,
        8.195929527282715,
        8.7536039352417,
        8.24117374420166,
        8.558771133422852,
        7.70729398727417,
        7.584288120269775,
        8.359525680541992,
        8.081310272216797,
        8.028738021850586,
        7.288191318511963,
        7.755941390991211,
        7.738576889038086,
        7.789920330047607,
        7.717297554016113,
        8.431472778320312,
        7.518991947174072,
        7.658801078796387,
        7.755782604217529,
        7.576831817626953,
        7.331742286682129,
        8.026237487792969,
        7.861719608306885,
        7.456665515899658,
        7.764540195465088,
        7.552800178527832,
        7.605340957641602,
        7.882884979248047,
        7.925989151000977,
        7.354263782501221,
        7.665863037109375,
        7.807674407958984,
        7.674951553344727,
        7.404209136962891,
        7.531030178070068,
        8.224337577819824,
        8.005525588989258,
        7.116026401519775,
        7.903189182281494,
        7.238913536071777,
        7.531999111175537,
        7.81131649017334,
    ],
    "real_score": [
        -0.013621438294649124,
        0.8799160122871399,
        3.119654655456543,
        4.031824111938477,
        5.389297008514404,
        6.047412395477295,
        4.955373287200928,
        5.209568977355957,
        6.346415042877197,
        7.090127468109131,
        7.044905662536621,
        7.523378372192383,
        4.309794902801514,
        4.5722737312316895,
        6.560158729553223,
        7.0498833656311035,
        5.228431224822998,
        5.973591327667236,
        6.277877330780029,
        8.03982925415039,
        8.825377464294434,
        9.058900833129883,
        8.176135063171387,
        9.450767517089844,
        2.4139273166656494,
        3.8656418323516846,
        4.349456787109375,
        5.057005405426025,
        5.422191143035889,
        6.283498764038086,
        6.893072128295898,
        5.91133451461792,
        6.0290961265563965,
        5.368997573852539,
        5.709414482116699,
        4.939642429351807,
        6.779411792755127,
        6.6616997718811035,
        7.127933979034424,
        7.413093090057373,
        7.850596904754639,
        7.705612659454346,
        8.044840812683105,
        0.2935006320476532,
        2.9566054344177246,
        3.9022605419158936,
        6.357597351074219,
        5.473474025726318,
        5.459425926208496,
        6.57785701751709,
    ],
    "fake_score": [
        -0.2310955822467804,
        -2.2838377952575684,
        -3.3815321922302246,
        -4.738895893096924,
        -5.472334861755371,
        -3.61472487449646,
        -5.371994972229004,
        -5.755106449127197,
        -6.344636917114258,
        -8.20427417755127,
        -6.779319763183594,
        -6.600273609161377,
        -2.5284368991851807,
        -4.644449710845947,
        -6.038994312286377,
        -6.034843444824219,
        -5.680476188659668,
        -6.823744773864746,
        -6.431984901428223,
        -8.642345428466797,
        -8.886600494384766,
        -9.568294525146484,
        -9.300675392150879,
        -8.494353294372559,
        -2.9307992458343506,
        -3.251284122467041,
        -4.303256034851074,
        -4.892312526702881,
        -7.04678201675415,
        -6.094773769378662,
        -7.549061298370361,
        -7.580185413360596,
        -4.811634540557861,
        -6.011552810668945,
        -5.858784198760986,
        -4.216360569000244,
        -7.493435382843018,
        -7.565021991729736,
        -7.448701858520508,
        -7.569988250732422,
        -8.33416748046875,
        -7.245410919189453,
        -9.48098373413086,
        -0.7189368009567261,
        -3.6877830028533936,
        -4.851955890655518,
        -5.693471431732178,
        -5.430876731872559,
        -5.9716267585754395,
        -6.13200044631958,
    ],
}


history2 = {
    "loss_g": [
        7.3720,
        7.5270,
        7.0569,
        7.5990,
        7.1792,
        8.1417,
        7.2140,
        7.4593,
        7.4313,
        7.6255,
    ],
    "loss_d": [
        1.7684e-02,
        1.2887e-03,
        1.0716e-03,
        3.9578e-03,
        1.3552e-03,
        7.6660e-01,
        1.4428e-02,
        6.0535e-02,
        1.5736e-03,
        3.7085e-02,
    ],
    "real_score": [
        7.3157e00,
        7.2464e00,
        7.1884e00,
        6.0117e00,
        7.3033e00,
        1.8951e-01,
        4.2998e00,
        3.7778e00,
        6.6303e00,
        4.4677e00,
    ],
    "fake_score": [
        -3.0220e00,
        -7.2703e00,
        -7.6720e00,
        -6.4103e00,
        -7.0463e00,
        9.4958e-02,
        -5.9356e00,
        -2.9378e00,
        -7.2591e00,
        -4.0342e00,
    ],
}


final = history1
for key in final.keys():
    final[key].extend(history2[key])
import json

print(json.dumps(final, indent=4))
print(f"the lenght of each element is : {len(final['loss_d'])} ")