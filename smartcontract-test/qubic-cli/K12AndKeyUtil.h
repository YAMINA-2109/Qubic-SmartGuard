#pragma once

#include <cstring>
#ifdef __aarch64__

#else
#include <immintrin.h>
#ifdef _MSC_VER
#include <intrin.h>
#endif
#endif
#include <cstdint>
#include <string>

#include "keyUtils.h"

#define ROL64(a, offset) ((((unsigned long long)a) << offset) ^ (((unsigned long long)a) >> (64 - offset)))

#define KeccakF1600RoundConstant0 0x000000008000808bULL
#define KeccakF1600RoundConstant1 0x800000000000008bULL
#define KeccakF1600RoundConstant2 0x8000000000008089ULL
#define KeccakF1600RoundConstant3 0x8000000000008003ULL
#define KeccakF1600RoundConstant4 0x8000000000008002ULL
#define KeccakF1600RoundConstant5 0x8000000000000080ULL
#define KeccakF1600RoundConstant6 0x000000000000800aULL
#define KeccakF1600RoundConstant7 0x800000008000000aULL
#define KeccakF1600RoundConstant8 0x8000000080008081ULL
#define KeccakF1600RoundConstant9 0x8000000000008080ULL
#define KeccakF1600RoundConstant10 0x0000000080000001ULL

#define declareABCDE                            \
    unsigned long long Aba, Abe, Abi, Abo, Abu; \
    unsigned long long Aga, Age, Agi, Ago, Agu; \
    unsigned long long Aka, Ake, Aki, Ako, Aku; \
    unsigned long long Ama, Ame, Ami, Amo, Amu; \
    unsigned long long Asa, Ase, Asi, Aso, Asu; \
    unsigned long long Bba, Bbe, Bbi, Bbo, Bbu; \
    unsigned long long Bga, Bge, Bgi, Bgo, Bgu; \
    unsigned long long Bka, Bke, Bki, Bko, Bku; \
    unsigned long long Bma, Bme, Bmi, Bmo, Bmu; \
    unsigned long long Bsa, Bse, Bsi, Bso, Bsu; \
    unsigned long long Ca, Ce, Ci, Co, Cu;      \
    unsigned long long Da, De, Di, Do, Du;      \
    unsigned long long Eba, Ebe, Ebi, Ebo, Ebu; \
    unsigned long long Ega, Ege, Egi, Ego, Egu; \
    unsigned long long Eka, Eke, Eki, Eko, Eku; \
    unsigned long long Ema, Eme, Emi, Emo, Emu; \
    unsigned long long Esa, Ese, Esi, Eso, Esu;

#define thetaRhoPiChiIotaPrepareTheta(i, A, E) \
    Da = Cu ^ ROL64(Ce, 1);                    \
    De = Ca ^ ROL64(Ci, 1);                    \
    Di = Ce ^ ROL64(Co, 1);                    \
    Do = Ci ^ ROL64(Cu, 1);                    \
    Du = Co ^ ROL64(Ca, 1);                    \
    A##ba ^= Da;                               \
    Bba = A##ba;                               \
    A##ge ^= De;                               \
    Bbe = ROL64(A##ge, 44);                    \
    A##ki ^= Di;                               \
    Bbi = ROL64(A##ki, 43);                    \
    A##mo ^= Do;                               \
    Bbo = ROL64(A##mo, 21);                    \
    A##su ^= Du;                               \
    Bbu = ROL64(A##su, 14);                    \
    E##ba = Bba ^ ((~Bbe) & Bbi);              \
    E##ba ^= KeccakF1600RoundConstant##i;      \
    Ca = E##ba;                                \
    E##be = Bbe ^ ((~Bbi) & Bbo);              \
    Ce = E##be;                                \
    E##bi = Bbi ^ ((~Bbo) & Bbu);              \
    Ci = E##bi;                                \
    E##bo = Bbo ^ ((~Bbu) & Bba);              \
    Co = E##bo;                                \
    E##bu = Bbu ^ ((~Bba) & Bbe);              \
    Cu = E##bu;                                \
    A##bo ^= Do;                               \
    Bga = ROL64(A##bo, 28);                    \
    A##gu ^= Du;                               \
    Bge = ROL64(A##gu, 20);                    \
    A##ka ^= Da;                               \
    Bgi = ROL64(A##ka, 3);                     \
    A##me ^= De;                               \
    Bgo = ROL64(A##me, 45);                    \
    A##si ^= Di;                               \
    Bgu = ROL64(A##si, 61);                    \
    E##ga = Bga ^ ((~Bge) & Bgi);              \
    Ca ^= E##ga;                               \
    E##ge = Bge ^ ((~Bgi) & Bgo);              \
    Ce ^= E##ge;                               \
    E##gi = Bgi ^ ((~Bgo) & Bgu);              \
    Ci ^= E##gi;                               \
    E##go = Bgo ^ ((~Bgu) & Bga);              \
    Co ^= E##go;                               \
    E##gu = Bgu ^ ((~Bga) & Bge);              \
    Cu ^= E##gu;                               \
    A##be ^= De;                               \
    Bka = ROL64(A##be, 1);                     \
    A##gi ^= Di;                               \
    Bke = ROL64(A##gi, 6);                     \
    A##ko ^= Do;                               \
    Bki = ROL64(A##ko, 25);                    \
    A##mu ^= Du;                               \
    Bko = ROL64(A##mu, 8);                     \
    A##sa ^= Da;                               \
    Bku = ROL64(A##sa, 18);                    \
    E##ka = Bka ^ ((~Bke) & Bki);              \
    Ca ^= E##ka;                               \
    E##ke = Bke ^ ((~Bki) & Bko);              \
    Ce ^= E##ke;                               \
    E##ki = Bki ^ ((~Bko) & Bku);              \
    Ci ^= E##ki;                               \
    E##ko = Bko ^ ((~Bku) & Bka);              \
    Co ^= E##ko;                               \
    E##ku = Bku ^ ((~Bka) & Bke);              \
    Cu ^= E##ku;                               \
    A##bu ^= Du;                               \
    Bma = ROL64(A##bu, 27);                    \
    A##ga ^= Da;                               \
    Bme = ROL64(A##ga, 36);                    \
    A##ke ^= De;                               \
    Bmi = ROL64(A##ke, 10);                    \
    A##mi ^= Di;                               \
    Bmo = ROL64(A##mi, 15);                    \
    A##so ^= Do;                               \
    Bmu = ROL64(A##so, 56);                    \
    E##ma = Bma ^ ((~Bme) & Bmi);              \
    Ca ^= E##ma;                               \
    E##me = Bme ^ ((~Bmi) & Bmo);              \
    Ce ^= E##me;                               \
    E##mi = Bmi ^ ((~Bmo) & Bmu);              \
    Ci ^= E##mi;                               \
    E##mo = Bmo ^ ((~Bmu) & Bma);              \
    Co ^= E##mo;                               \
    E##mu = Bmu ^ ((~Bma) & Bme);              \
    Cu ^= E##mu;                               \
    A##bi ^= Di;                               \
    Bsa = ROL64(A##bi, 62);                    \
    A##go ^= Do;                               \
    Bse = ROL64(A##go, 55);                    \
    A##ku ^= Du;                               \
    Bsi = ROL64(A##ku, 39);                    \
    A##ma ^= Da;                               \
    Bso = ROL64(A##ma, 41);                    \
    A##se ^= De;                               \
    Bsu = ROL64(A##se, 2);                     \
    E##sa = Bsa ^ ((~Bse) & Bsi);              \
    Ca ^= E##sa;                               \
    E##se = Bse ^ ((~Bsi) & Bso);              \
    Ce ^= E##se;                               \
    E##si = Bsi ^ ((~Bso) & Bsu);              \
    Ci ^= E##si;                               \
    E##so = Bso ^ ((~Bsu) & Bsa);              \
    Co ^= E##so;                               \
    E##su = Bsu ^ ((~Bsa) & Bse);              \
    Cu ^= E##su;

#define copyFromState(state) \
    Aba = state[0];          \
    Abe = state[1];          \
    Abi = state[2];          \
    Abo = state[3];          \
    Abu = state[4];          \
    Aga = state[5];          \
    Age = state[6];          \
    Agi = state[7];          \
    Ago = state[8];          \
    Agu = state[9];          \
    Aka = state[10];         \
    Ake = state[11];         \
    Aki = state[12];         \
    Ako = state[13];         \
    Aku = state[14];         \
    Ama = state[15];         \
    Ame = state[16];         \
    Ami = state[17];         \
    Amo = state[18];         \
    Amu = state[19];         \
    Asa = state[20];         \
    Ase = state[21];         \
    Asi = state[22];         \
    Aso = state[23];         \
    Asu = state[24];

#define copyToState(state) \
    state[0] = Aba;        \
    state[1] = Abe;        \
    state[2] = Abi;        \
    state[3] = Abo;        \
    state[4] = Abu;        \
    state[5] = Aga;        \
    state[6] = Age;        \
    state[7] = Agi;        \
    state[8] = Ago;        \
    state[9] = Agu;        \
    state[10] = Aka;       \
    state[11] = Ake;       \
    state[12] = Aki;       \
    state[13] = Ako;       \
    state[14] = Aku;       \
    state[15] = Ama;       \
    state[16] = Ame;       \
    state[17] = Ami;       \
    state[18] = Amo;       \
    state[19] = Amu;       \
    state[20] = Asa;       \
    state[21] = Ase;       \
    state[22] = Asi;       \
    state[23] = Aso;       \
    state[24] = Asu;

#define rounds12                                                                    \
    Ca = Aba ^ Aga ^ Aka ^ Ama ^ Asa;                                               \
    Ce = Abe ^ Age ^ Ake ^ Ame ^ Ase;                                               \
    Ci = Abi ^ Agi ^ Aki ^ Ami ^ Asi;                                               \
    Co = Abo ^ Ago ^ Ako ^ Amo ^ Aso;                                               \
    Cu = Abu ^ Agu ^ Aku ^ Amu ^ Asu;                                               \
    thetaRhoPiChiIotaPrepareTheta(0, A, E)                                          \
        thetaRhoPiChiIotaPrepareTheta(1, E, A)                                      \
            thetaRhoPiChiIotaPrepareTheta(2, A, E)                                  \
                thetaRhoPiChiIotaPrepareTheta(3, E, A)                              \
                    thetaRhoPiChiIotaPrepareTheta(4, A, E)                          \
                        thetaRhoPiChiIotaPrepareTheta(5, E, A)                      \
                            thetaRhoPiChiIotaPrepareTheta(6, A, E)                  \
                                thetaRhoPiChiIotaPrepareTheta(7, E, A)              \
                                    thetaRhoPiChiIotaPrepareTheta(8, A, E)          \
                                        thetaRhoPiChiIotaPrepareTheta(9, E, A)      \
                                            thetaRhoPiChiIotaPrepareTheta(10, A, E) \
                                                Da = Cu ^ ROL64(Ce, 1);             \
    De = Ca ^ ROL64(Ci, 1);                                                         \
    Di = Ce ^ ROL64(Co, 1);                                                         \
    Do = Ci ^ ROL64(Cu, 1);                                                         \
    Du = Co ^ ROL64(Ca, 1);                                                         \
    Eba ^= Da;                                                                      \
    Bba = Eba;                                                                      \
    Ege ^= De;                                                                      \
    Bbe = ROL64(Ege, 44);                                                           \
    Eki ^= Di;                                                                      \
    Bbi = ROL64(Eki, 43);                                                           \
    Emo ^= Do;                                                                      \
    Bbo = ROL64(Emo, 21);                                                           \
    Esu ^= Du;                                                                      \
    Bbu = ROL64(Esu, 14);                                                           \
    Aba = Bba ^ ((~Bbe) & Bbi);                                                     \
    Aba ^= 0x8000000080008008ULL;                                                   \
    Abe = Bbe ^ ((~Bbi) & Bbo);                                                     \
    Abi = Bbi ^ ((~Bbo) & Bbu);                                                     \
    Abo = Bbo ^ ((~Bbu) & Bba);                                                     \
    Abu = Bbu ^ ((~Bba) & Bbe);                                                     \
    Ebo ^= Do;                                                                      \
    Bga = ROL64(Ebo, 28);                                                           \
    Egu ^= Du;                                                                      \
    Bge = ROL64(Egu, 20);                                                           \
    Eka ^= Da;                                                                      \
    Bgi = ROL64(Eka, 3);                                                            \
    Eme ^= De;                                                                      \
    Bgo = ROL64(Eme, 45);                                                           \
    Esi ^= Di;                                                                      \
    Bgu = ROL64(Esi, 61);                                                           \
    Aga = Bga ^ ((~Bge) & Bgi);                                                     \
    Age = Bge ^ ((~Bgi) & Bgo);                                                     \
    Agi = Bgi ^ ((~Bgo) & Bgu);                                                     \
    Ago = Bgo ^ ((~Bgu) & Bga);                                                     \
    Agu = Bgu ^ ((~Bga) & Bge);                                                     \
    Ebe ^= De;                                                                      \
    Bka = ROL64(Ebe, 1);                                                            \
    Egi ^= Di;                                                                      \
    Bke = ROL64(Egi, 6);                                                            \
    Eko ^= Do;                                                                      \
    Bki = ROL64(Eko, 25);                                                           \
    Emu ^= Du;                                                                      \
    Bko = ROL64(Emu, 8);                                                            \
    Esa ^= Da;                                                                      \
    Bku = ROL64(Esa, 18);                                                           \
    Aka = Bka ^ ((~Bke) & Bki);                                                     \
    Ake = Bke ^ ((~Bki) & Bko);                                                     \
    Aki = Bki ^ ((~Bko) & Bku);                                                     \
    Ako = Bko ^ ((~Bku) & Bka);                                                     \
    Aku = Bku ^ ((~Bka) & Bke);                                                     \
    Ebu ^= Du;                                                                      \
    Bma = ROL64(Ebu, 27);                                                           \
    Ega ^= Da;                                                                      \
    Bme = ROL64(Ega, 36);                                                           \
    Eke ^= De;                                                                      \
    Bmi = ROL64(Eke, 10);                                                           \
    Emi ^= Di;                                                                      \
    Bmo = ROL64(Emi, 15);                                                           \
    Eso ^= Do;                                                                      \
    Bmu = ROL64(Eso, 56);                                                           \
    Ama = Bma ^ ((~Bme) & Bmi);                                                     \
    Ame = Bme ^ ((~Bmi) & Bmo);                                                     \
    Ami = Bmi ^ ((~Bmo) & Bmu);                                                     \
    Amo = Bmo ^ ((~Bmu) & Bma);                                                     \
    Amu = Bmu ^ ((~Bma) & Bme);                                                     \
    Ebi ^= Di;                                                                      \
    Bsa = ROL64(Ebi, 62);                                                           \
    Ego ^= Do;                                                                      \
    Bse = ROL64(Ego, 55);                                                           \
    Eku ^= Du;                                                                      \
    Bsi = ROL64(Eku, 39);                                                           \
    Ema ^= Da;                                                                      \
    Bso = ROL64(Ema, 41);                                                           \
    Ese ^= De;                                                                      \
    Bsu = ROL64(Ese, 2);                                                            \
    Asa = Bsa ^ ((~Bse) & Bsi);                                                     \
    Ase = Bse ^ ((~Bsi) & Bso);                                                     \
    Asi = Bsi ^ ((~Bso) & Bsu);                                                     \
    Aso = Bso ^ ((~Bsu) & Bsa);                                                     \
    Asu = Bsu ^ ((~Bsa) & Bse);

#define K12_security 128
#define K12_capacity (2 * K12_security)
#define K12_capacityInBytes (K12_capacity / 8)
#define K12_rateInBytes ((1600 - K12_capacity) / 8)
#define K12_chunkSize 8192
#define K12_suffixLeaf 0x0B

typedef struct
{
    uint8_t state[200];
    uint8_t byteIOIndex;
} KangarooTwelve_F;

static void KeccakP1600_Permute_12rounds(uint8_t *state)
{
    declareABCDE unsigned long long *stateAsLanes = (unsigned long long *)state;
    copyFromState(stateAsLanes)
    rounds12
    copyToState(stateAsLanes)
}

static void KangarooTwelve_F_Absorb(KangarooTwelve_F *instance, const uint8_t *data, unsigned long long dataByteLen)
{
    unsigned long long i = 0;
    while (i < dataByteLen)
    {
        if (!instance->byteIOIndex && dataByteLen >= i + K12_rateInBytes)
        {
            declareABCDE unsigned long long *stateAsLanes = (unsigned long long *)instance->state;
            copyFromState(stateAsLanes)
            unsigned long long modifiedDataByteLen = dataByteLen - i;
            while (modifiedDataByteLen >= K12_rateInBytes)
            {
                Aba ^= ((unsigned long long *)data)[0];
                Abe ^= ((unsigned long long *)data)[1];
                Abi ^= ((unsigned long long *)data)[2];
                Abo ^= ((unsigned long long *)data)[3];
                Abu ^= ((unsigned long long *)data)[4];
                Aga ^= ((unsigned long long *)data)[5];
                Age ^= ((unsigned long long *)data)[6];
                Agi ^= ((unsigned long long *)data)[7];
                Ago ^= ((unsigned long long *)data)[8];
                Agu ^= ((unsigned long long *)data)[9];
                Aka ^= ((unsigned long long *)data)[10];
                Ake ^= ((unsigned long long *)data)[11];
                Aki ^= ((unsigned long long *)data)[12];
                Ako ^= ((unsigned long long *)data)[13];
                Aku ^= ((unsigned long long *)data)[14];
                Ama ^= ((unsigned long long *)data)[15];
                Ame ^= ((unsigned long long *)data)[16];
                Ami ^= ((unsigned long long *)data)[17];
                Amo ^= ((unsigned long long *)data)[18];
                Amu ^= ((unsigned long long *)data)[19];
                Asa ^= ((unsigned long long *)data)[20];
                rounds12
                data += K12_rateInBytes;
                modifiedDataByteLen -= K12_rateInBytes;
            }
            copyToState(stateAsLanes)
            i = dataByteLen - modifiedDataByteLen;
        }
        else
        {
            uint8_t partialBlock;
            if ((dataByteLen - i) + instance->byteIOIndex > K12_rateInBytes)
            {
                partialBlock = K12_rateInBytes - instance->byteIOIndex;
            }
            else
            {
                partialBlock = (uint8_t)(dataByteLen - i);
            }
            i += partialBlock;

            if (!instance->byteIOIndex)
            {
                unsigned int j = 0;
                for (; (j + 8) <= (unsigned int)(partialBlock >> 3); j += 8)
                {
                    ((unsigned long long *)instance->state)[j + 0] ^= ((unsigned long long *)data)[j + 0];
                    ((unsigned long long *)instance->state)[j + 1] ^= ((unsigned long long *)data)[j + 1];
                    ((unsigned long long *)instance->state)[j + 2] ^= ((unsigned long long *)data)[j + 2];
                    ((unsigned long long *)instance->state)[j + 3] ^= ((unsigned long long *)data)[j + 3];
                    ((unsigned long long *)instance->state)[j + 4] ^= ((unsigned long long *)data)[j + 4];
                    ((unsigned long long *)instance->state)[j + 5] ^= ((unsigned long long *)data)[j + 5];
                    ((unsigned long long *)instance->state)[j + 6] ^= ((unsigned long long *)data)[j + 6];
                    ((unsigned long long *)instance->state)[j + 7] ^= ((unsigned long long *)data)[j + 7];
                }
                for (; (j + 4) <= (unsigned int)(partialBlock >> 3); j += 4)
                {
                    ((unsigned long long *)instance->state)[j + 0] ^= ((unsigned long long *)data)[j + 0];
                    ((unsigned long long *)instance->state)[j + 1] ^= ((unsigned long long *)data)[j + 1];
                    ((unsigned long long *)instance->state)[j + 2] ^= ((unsigned long long *)data)[j + 2];
                    ((unsigned long long *)instance->state)[j + 3] ^= ((unsigned long long *)data)[j + 3];
                }
                for (; (j + 2) <= (unsigned int)(partialBlock >> 3); j += 2)
                {
                    ((unsigned long long *)instance->state)[j + 0] ^= ((unsigned long long *)data)[j + 0];
                    ((unsigned long long *)instance->state)[j + 1] ^= ((unsigned long long *)data)[j + 1];
                }
                if (j < (unsigned int)(partialBlock >> 3))
                {
                    ((unsigned long long *)instance->state)[j + 0] ^= ((unsigned long long *)data)[j + 0];
                }
                if (partialBlock & 7)
                {
                    unsigned long long lane = 0;
                    memcpy(&lane, data + (partialBlock & 0xFFFFFFF8), partialBlock & 7);
                    ((unsigned long long *)instance->state)[partialBlock >> 3] ^= lane;
                }
            }
            else
            {
                unsigned int _sizeLeft = partialBlock;
                unsigned int _lanePosition = instance->byteIOIndex >> 3;
                unsigned int _offsetInLane = instance->byteIOIndex & 7;
                const uint8_t *_curData = data;
                while (_sizeLeft > 0)
                {
                    unsigned int _bytesInLane = 8 - _offsetInLane;
                    if (_bytesInLane > _sizeLeft)
                    {
                        _bytesInLane = _sizeLeft;
                    }
                    if (_bytesInLane)
                    {
                        unsigned long long lane = 0;
                        memcpy(&lane, (void *)_curData, _bytesInLane);
                        ((unsigned long long *)instance->state)[_lanePosition] ^= (lane << (_offsetInLane << 3));
                    }
                    _sizeLeft -= _bytesInLane;
                    _lanePosition++;
                    _offsetInLane = 0;
                    _curData += _bytesInLane;
                }
            }

            data += partialBlock;
            instance->byteIOIndex += partialBlock;
            if (instance->byteIOIndex == K12_rateInBytes)
            {
                KeccakP1600_Permute_12rounds(instance->state);
                instance->byteIOIndex = 0;
            }
        }
    }
}

static void KangarooTwelve(const uint8_t *input, unsigned int inputByteLen, uint8_t *output, unsigned int outputByteLen)
{
    KangarooTwelve_F queueNode;
    KangarooTwelve_F finalNode;
    unsigned int blockNumber, queueAbsorbedLen;

    memset(&finalNode, 0, sizeof(KangarooTwelve_F));
    const unsigned int len = inputByteLen ^ ((K12_chunkSize ^ inputByteLen) & -(K12_chunkSize < inputByteLen));
    KangarooTwelve_F_Absorb(&finalNode, input, len);
    input += len;
    inputByteLen -= len;
    if (len == K12_chunkSize && inputByteLen)
    {
        blockNumber = 1;
        queueAbsorbedLen = 0;
        finalNode.state[finalNode.byteIOIndex] ^= 0x03;
        if (++finalNode.byteIOIndex == K12_rateInBytes)
        {
            KeccakP1600_Permute_12rounds(finalNode.state);
            finalNode.byteIOIndex = 0;
        }
        else
        {
            finalNode.byteIOIndex = (finalNode.byteIOIndex + 7) & ~7;
        }

        while (inputByteLen > 0)
        {
            const unsigned int len = K12_chunkSize ^ ((inputByteLen ^ K12_chunkSize) & -(inputByteLen < K12_chunkSize));
            memset(&queueNode, 0, sizeof(KangarooTwelve_F));
            KangarooTwelve_F_Absorb(&queueNode, input, len);
            input += len;
            inputByteLen -= len;
            if (len == K12_chunkSize)
            {
                ++blockNumber;
                queueNode.state[queueNode.byteIOIndex] ^= K12_suffixLeaf;
                queueNode.state[K12_rateInBytes - 1] ^= 0x80;
                KeccakP1600_Permute_12rounds(queueNode.state);
                queueNode.byteIOIndex = K12_capacityInBytes;
                KangarooTwelve_F_Absorb(&finalNode, queueNode.state, K12_capacityInBytes);
            }
            else
            {
                queueAbsorbedLen = len;
            }
        }

        if (queueAbsorbedLen)
        {
            if (++queueNode.byteIOIndex == K12_rateInBytes)
            {
                KeccakP1600_Permute_12rounds(queueNode.state);
                queueNode.byteIOIndex = 0;
            }
            if (++queueAbsorbedLen == K12_chunkSize)
            {
                ++blockNumber;
                queueAbsorbedLen = 0;
                queueNode.state[queueNode.byteIOIndex] ^= K12_suffixLeaf;
                queueNode.state[K12_rateInBytes - 1] ^= 0x80;
                KeccakP1600_Permute_12rounds(queueNode.state);
                queueNode.byteIOIndex = K12_capacityInBytes;
                KangarooTwelve_F_Absorb(&finalNode, queueNode.state, K12_capacityInBytes);
            }
        }
        else
        {
            memset(queueNode.state, 0, sizeof(queueNode.state));
            queueNode.byteIOIndex = 1;
            queueAbsorbedLen = 1;
        }
    }
    else
    {
        if (len == K12_chunkSize)
        {
            blockNumber = 1;
            finalNode.state[finalNode.byteIOIndex] ^= 0x03;
            if (++finalNode.byteIOIndex == K12_rateInBytes)
            {
                KeccakP1600_Permute_12rounds(finalNode.state);
                finalNode.byteIOIndex = 0;
            }
            else
            {
                finalNode.byteIOIndex = (finalNode.byteIOIndex + 7) & ~7;
            }

            memset(queueNode.state, 0, sizeof(queueNode.state));
            queueNode.byteIOIndex = 1;
            queueAbsorbedLen = 1;
        }
        else
        {
            blockNumber = 0;
            if (++finalNode.byteIOIndex == K12_rateInBytes)
            {
                KeccakP1600_Permute_12rounds(finalNode.state);
                finalNode.state[0] ^= 0x07;
            }
            else
            {
                finalNode.state[finalNode.byteIOIndex] ^= 0x07;
            }
        }
    }

    if (blockNumber)
    {
        if (queueAbsorbedLen)
        {
            blockNumber++;
            queueNode.state[queueNode.byteIOIndex] ^= K12_suffixLeaf;
            queueNode.state[K12_rateInBytes - 1] ^= 0x80;
            KeccakP1600_Permute_12rounds(queueNode.state);
            KangarooTwelve_F_Absorb(&finalNode, queueNode.state, K12_capacityInBytes);
        }
        unsigned int n = 0;
        for (unsigned long long v = --blockNumber; v && (n < sizeof(unsigned long long)); ++n, v >>= 8)
        {
        }
        uint8_t encbuf[sizeof(unsigned long long) + 1 + 2];
        for (unsigned int i = 1; i <= n; ++i)
        {
            encbuf[i - 1] = (uint8_t)(blockNumber >> (8 * (n - i)));
        }
        encbuf[n] = (uint8_t)n;
        encbuf[++n] = 0xFF;
        encbuf[++n] = 0xFF;
        KangarooTwelve_F_Absorb(&finalNode, encbuf, ++n);
        finalNode.state[finalNode.byteIOIndex] ^= 0x06;
    }
    finalNode.state[K12_rateInBytes - 1] ^= 0x80;
    KeccakP1600_Permute_12rounds(finalNode.state);
    memcpy(output, finalNode.state, outputByteLen);
}
#define CURVE_ORDER_0 0x2FB2540EC7768CE7
#define CURVE_ORDER_1 0xDFBD004DFE0F7999
#define CURVE_ORDER_2 0xF05397829CBC14E5
#define CURVE_ORDER_3 0x0029CBC14E5E0A72
#define MONTGOMERY_SMALL_R_PRIME_0 0xE12FE5F079BC3929
#define MONTGOMERY_SMALL_R_PRIME_1 0xD75E78B8D1FCDCF3
#define MONTGOMERY_SMALL_R_PRIME_2 0xBCE409ED76B5DB21
#define MONTGOMERY_SMALL_R_PRIME_3 0xF32702FDAFC1C074

#define B11 0xF6F900D81F5F5E6A
#define B12 0x1363E862C22A2DA0
#define B13 0xF8BD9FCE1337FCF1
#define B14 0x084F739986B9E651
#define B21 0xE2B6A4157B033D2C
#define B22 0x0000000000000001
#define B23 0xFFFFFFFFFFFFFFFF
#define B24 0xDA243A43722E9830
#define B31 0xE85452E2DCE0FCFE
#define B32 0xFD3BDEE51C7725AF
#define B33 0x2E4D21C98927C49F
#define B34 0xF56190BB3FD13269
#define B41 0xEC91CBF56EF737C1
#define B42 0xCEDD20D23C1F00CE
#define B43 0x068A49F02AA8A9B5
#define B44 0x18D5087896DE0AEA
#define C1 0x72482C5251A4559C
#define C2 0x59F95B0ADD276F6C
#define C3 0x7DD2D17C4625FA78
#define C4 0x6BC57DEF56CE8877
#ifndef BUILD_4Q_LIB
typedef unsigned long long felm_t[2]; // Datatype for representing 128-bit field elements
typedef felm_t f2elm_t[2]; // Datatype for representing quadratic extension field elements
typedef struct
{ // Point representation in affine coordinates
    f2elm_t x;
    f2elm_t y;
} point_affine;
typedef point_affine point_t[1];
#define VOID_FUNC_DECL static void
#define BOOL_FUNC_DECL static bool
#else
#define VOID_FUNC_DECL void
#define BOOL_FUNC_DECL bool
#endif

typedef struct
{ // Point representation in extended coordinates
    f2elm_t x;
    f2elm_t y;
    f2elm_t z;
    f2elm_t ta;
    f2elm_t tb;
} point_extproj;
typedef point_extproj point_extproj_t[1];

typedef struct
{ // Point representation in extended coordinates (for precomputed points)
    f2elm_t xy;
    f2elm_t yx;
    f2elm_t z2;
    f2elm_t t2;
} point_extproj_precomp;
typedef point_extproj_precomp point_extproj_precomp_t[1];

typedef struct
{ // Point representation in extended affine coordinates (for precomputed points)
    f2elm_t xy;
    f2elm_t yx;
    f2elm_t t2;
} point_precomp;
typedef point_precomp point_precomp_t[1];

static const unsigned long long PARAMETER_d[4] = { 0x0000000000000142, 0x00000000000000E4, 0xB3821488F1FC0C8D, 0x5E472F846657E0FC };
static const unsigned long long curve_order[4] = { CURVE_ORDER_0, CURVE_ORDER_1, CURVE_ORDER_2, CURVE_ORDER_3 };
static const unsigned long long Montgomery_Rprime[4] = { 0xC81DB8795FF3D621, 0x173EA5AAEA6B387D, 0x3D01B7C72136F61C, 0x0006A5F16AC8F9D3 };
static const unsigned long long ONE[4] = { 1, 0, 0, 0 };

// Fixed GF(p^2) constants for the endomorphisms
static const unsigned long long ctau1[4] = { 0x74DCD57CEBCE74C3, 0x1964DE2C3AFAD20C, 0x12, 0x0C };
static const unsigned long long ctaudual1[4] = { 0x9ECAA6D9DECDF034, 0x4AA740EB23058652, 0x11, 0x7FFFFFFFFFFFFFF4 };
static const unsigned long long cphi0[4] = { 0xFFFFFFFFFFFFFFF7, 0x05, 0x4F65536CEF66F81A, 0x2553A0759182C329 };
static const unsigned long long cphi1[4] = { 0x07, 0x05, 0x334D90E9E28296F9, 0x62C8CAA0C50C62CF };
static const unsigned long long cphi2[4] = { 0x15, 0x0F, 0x2C2CB7154F1DF391, 0x78DF262B6C9B5C98 };
static const unsigned long long cphi3[4] = { 0x03, 0x02, 0x92440457A7962EA4, 0x5084C6491D76342A };
static const unsigned long long cphi4[4] = { 0x03, 0x03, 0xA1098C923AEC6855, 0x12440457A7962EA4 };
static const unsigned long long cphi5[4] = { 0x0F, 0x0A, 0x669B21D3C5052DF3, 0x459195418A18C59E };
static const unsigned long long cphi6[4] = { 0x18, 0x12, 0xCD3643A78A0A5BE7, 0x0B232A8314318B3C };
static const unsigned long long cphi7[4] = { 0x23, 0x18, 0x66C183035F48781A, 0x3963BC1C99E2EA1A };
static const unsigned long long cphi8[4] = { 0xF0, 0xAA, 0x44E251582B5D0EF0, 0x1F529F860316CBE5 };
static const unsigned long long cphi9[4] = { 0xBEF, 0x870, 0x14D3E48976E2505, 0xFD52E9CFE00375B };
static const unsigned long long cpsi1[4] = { 0xEDF07F4767E346EF, 0x2AF99E9A83D54A02, 0x13A, 0xDE };
static const unsigned long long cpsi2[4] = { 0x143, 0xE4, 0x4C7DEB770E03F372, 0x21B8D07B99A81F03 };
static const unsigned long long cpsi3[4] = { 0x09, 0x06, 0x3A6E6ABE75E73A61, 0x4CB26F161D7D6906 };
static const unsigned long long cpsi4[4] = { 0xFFFFFFFFFFFFFFF6, 0x7FFFFFFFFFFFFFF9, 0xC59195418A18C59E, 0x334D90E9E28296F9 };

// Precomputed integers for fast-Babai rounding
static const unsigned long long ell1[4] = { 0x259686E09D1A7D4F, 0xF75682ACE6A6BD66, 0xFC5BB5C5EA2BE5DF, 0x07 };
static const unsigned long long ell2[4] = { 0xD1BA1D84DD627AFB, 0x2BD235580F468D8D, 0x8FD4B04CAA6C0F8A, 0x03 };
static const unsigned long long ell3[4] = { 0x9B291A33678C203C, 0xC42BD6C965DCA902, 0xD038BF8D0BFFBAF6, 0x00 };
static const unsigned long long ell4[4] = { 0x12E5666B77E7FDC0, 0x81CBDC3714983D82, 0x1B073877A22D8410, 0x03 };

// The table below was generated using window width W = 5 and table parameter V = 5 (see http://eprint.iacr.org/2013/158).
// Number of point entries = 5 * 2^4 = 80 points, where each point (x,y) is represented using coordinates (x+y,y-x,2*d*t).
// Table size = 80 * 3 * 256 = 7.5KB
static const unsigned long long FIXED_BASE_TABLE[960] = {
        0xe18a34f3a703e631, 0x287460bf1d502b5f, 0xe02e62f7e4f90353, 0x0c3ba0378b86acde, 0x90bf0f98b0937edc, 0x740b7c7824f0c555, 0xb321239123a01366, 0x4ffcf5b93a9557a5, 0x297afccbabda42bb, 0x5948d137556c97c6, 0xa8189a393330684c, 0x0caf2b720a341f27
        , 0x3a8ba018fd188787, 0x5546128188dd12a8, 0xb0b3cc33c09f9b77, 0x1baeeaf8b84d2049, 0x006425a611faf900, 0x18f7cd12e1a6f789, 0x6dccf09a12556066, 0x448e05eeace7b6eb, 0xbf2f33689d2829b0, 0x6d911dcb2957bdb4, 0x9f2353dbdc3c03ee, 0x06c54305babee501
        , 0x2eaf45713dafa125, 0x72963058648a364d, 0x61b7771f9d313ef2, 0x4f41c7f8bfe2b069, 0x408623ae599790ac, 0x4d33858644330a42, 0xfc5696649cdd7487, 0x74df72e0e598e114, 0xc9a06325913c110b, 0x076bd4115fe4b0d8, 0x76619e65d6bff3d9, 0x249240147cee3a08
        , 0xd695b96148965a73, 0x28aac8a28829f706, 0x41f1c05329f7a57b, 0x441ca9e89f03e00e, 0xe1aa38ab8bf7241e, 0x58f28cafc832b7f4, 0xcadaf8b8fa5400c6, 0x34b6d106284e863e, 0xf5498cab3af15097, 0x6dbe7790017d9c49, 0x63bf76a81448e8bc, 0x6371925bf23ae006
        , 0xc5e2c721bded81fa, 0x4ede70eed68056ab, 0x8f3cd9b5b4975810, 0x4752fd192f0a9aa8, 0x318794eb1f734414, 0x11ddf7d2c8468662, 0x2613b06f72b1a34e, 0x465575b37ab06770, 0x40b9845f82638d2b, 0x48894050790298ce, 0xbedb93a501b4f131, 0x04f3560d2889b2fb
        , 0x457dd875115b278b, 0x56f25ee54d92858a, 0x92d4c1cdce0c977e, 0x078fca4187d74996, 0x3bbb2ded76cc22a1, 0x117b28853ddc2bf6, 0x43f3767cb9c2baa2, 0x73079e25e0ea8a8f, 0x0177992b5a15796d, 0x2e77721480d9ef92, 0xbe09883567372916, 0x258f176b7af7576d
        , 0x308338fd6168391b, 0x7285925f9a7353a4, 0x862c0fd04fe85114, 0x53259ee7423aeb51, 0xfe0031a84b3b1a68, 0x1a4f1d661fa071fc, 0x2ddd54168dc928a7, 0x60185c1adf196a6a, 0x49809717dc6da9b4, 0x6062094b4dcffc03, 0xa41ea6fa05fa7e8d, 0x4a4fe06f277148a0
        , 0x7bb253a9ee9e80f0, 0x419a928bccb11733, 0x84323be66a9a039e, 0x01b2d1ae972814bb, 0xa7588584d3051231, 0x54df1e20cc979dd7, 0x91d906fe3e2f22dd, 0x4e36e9975fdf1a0f, 0xd81871746b747634, 0x3e5e31baeee13433, 0xe4da80979573baa3, 0x4b852ad97cfe77c6
        , 0xe08b346714418b9e, 0x283d719b2fe6ef88, 0xb7339d2de45c180b, 0x75acfcef11d2d5c8, 0x8f40777a8c561876, 0x0c54ac40a7134c4b, 0xb92e287d66baee08, 0x6f357e5006a188bf, 0xc5903319ed1e6971, 0x747c45ef91dafd40, 0xde4086a91d2f816e, 0x5dcb27edb3b3ef7d
        , 0x43fdc46cfa1dd2ee, 0x51551f9f70966498, 0xb54534f761ed9bdc, 0x453455b3073fb07f, 0xf24773e383cab70b, 0x679be25e758cf4df, 0xda17edf2943eee29, 0x3dc9e5b8d6dc0f66, 0x56a50cba413fb75b, 0x1e65315bc5a8537f, 0x5ff90242802c7213, 0x73c9d8c8f425252e
        , 0x3c637b8633198c8f, 0x534f84b3ed414f33, 0xad313e72dedd6902, 0x5ed57e941cdf33af, 0x5a6fe01d2a57306e, 0x73b63dea344713f9, 0x39cb70570f1c2bf3, 0x2df8c6e49f1a18db, 0x661bc349677797e4, 0x501ae7cbbebe9062, 0x5b52a88de8959643, 0x0372752811c01d51
        , 0x010c57a2301bb928, 0x378b317155554fc6, 0xf883fa4229a02cf1, 0x5f0047b850d7db29, 0x4d247ae328402daa, 0x0d030627a850a2bc, 0xb4e65d9a88a443f5, 0x6ec9686b2d6db089, 0xde202e08fea1d987, 0x5c64e1d3f28d7600, 0x157d17bef661bfb7, 0x56392d36dd75334c
        , 0xe25478d8bd19155c, 0x146d4f2d3d336afd, 0x9bfbe00bf94e15e8, 0x2b185a9a6adf10c0, 0x926527b3ed52ab7b, 0x67997e1473101e80, 0xb58f4ff4947cc541, 0x36f800c7fac99a7a, 0xd0302e32400456d9, 0x4372e43640bc697b, 0x9144cabb4750d898, 0x75d25afac9a23cbf
        , 0x794591767655cbfe, 0x74db216617fc4b07, 0x7057b2242566d0c9, 0x1d543b5908417b23, 0x19c280b444428783, 0x352309fd8b6cc3ef, 0x37833d6ac068ae72, 0x4ec0671a23c019f4, 0x9d9836e1a3d05bb5, 0x44fe1adff224efe3, 0xa296bc3ce57efb4a, 0x2efec86835a14150
        , 0x2fe19c09fb194bca, 0x18cc07d3953cd206, 0x5bdff217c9c0b9e0, 0x671aa756581abcee, 0xe1cc33ae28f7d1a2, 0x1b6f254937a0a3fe, 0x51503d1665babb83, 0x74b95636d5889211, 0xbdb97ae4ea96f869, 0x1507ce189e2510bd, 0x796e4d54fab93b13, 0x6a81765f05960929
        , 0x2e940521e5a833ed, 0x3bdea532b245f644, 0xbea76975ffd52693, 0x64b94848ba6d4ed6, 0x9db52d0194e33ec7, 0x71cf65da55639f25, 0xede73b1fdb5a8138, 0x12e4d13b6c62dc22, 0x9d19b0c265185517, 0x77a011d257b5fdd0, 0x1fedc5caaecd84e4, 0x46844e151e3492d1
        , 0x7a423a31904220df, 0x5b3165c747e8f099, 0x1c665eeadf35e22e, 0x7802b556fc45595b, 0x85a2def4015bd2de, 0x17f2ab87957166ad, 0x19cf6d352060c1e5, 0x122a7ad1be408e6a, 0x5b79bbc8645bf766, 0x20fb009d4d0adacf, 0x97526a272ba28538, 0x7041b4e90d420bde
        , 0x3b30113358dab057, 0x3d398b66f0d24243, 0x91a5999a03cd4708, 0x1eae2409cd938096, 0x66dd6b604c36108c, 0x1713083789081968, 0x57cad6917125dcfd, 0x34b06cb89704f1ca, 0xdcafe8e71f35abf2, 0x698331198d544db9, 0x6287676643af075b, 0x200950e5559d2b6d
        , 0xd4f63fc3ecdd9074, 0x7473317142ac13a2, 0x96b0030805319356, 0x2c20ffe0244378ba, 0x4889511ad26ac01a, 0x4ee327219997fcf6, 0x15ffe6e70f0bf8ea, 0x6b617fb4a6d0a6d7, 0x4916dca1c52f7324, 0x3c8269f086468277, 0xc24210c4c837e04b, 0x4e480b4f915a542c
        , 0xc5fef3b09a7fe35e, 0x31a501de44fd84b2, 0x79f29e4940a407b9, 0x0ba7e03ca5cce5ab, 0xa7a8b2058a74d8ea, 0x46f4c7810e26dadc, 0x46171ace94a1128a, 0x44db55025495a811, 0x7f889e1a4bf18d5c, 0x4d4f172a43f306b2, 0x33a99766bb1cffad, 0x6254775924d39aca
        , 0xd855230ec225136e, 0x1c544dd078d9211d, 0x12fe9969f63f63ba, 0x069af1dc949dd382, 0x305bcf40cfe5c256, 0x63ae90924bbbb595, 0xe451097793b7de06, 0x09780cf39fc0043e, 0x827af8e7eb798871, 0x3ace8a6c77577a37, 0x79df061332e055ba, 0x561dc07aaacea92b
        , 0x7e4422d9820d2673, 0x6b85df83e0af5348, 0x1f151ac1ded8526b, 0x35ead8e5157142bd, 0x6da6ef6c33c79dd4, 0x5f2ea04d2594fde4, 0x91037d0cc027d5fa, 0x53b5401007b0331b, 0x810f198a3d4ba5a3, 0x4463bd259ba94195, 0x32b894acec2acf9e, 0x78711761d64349ce
        , 0x253ae1b3f51fe211, 0x409e4b3f535b6463, 0x3a236d10da5e49de, 0x19d2b1029c21336a, 0x2835f40436aadd90, 0x0942a31505190b19, 0xc189131876828279, 0x3afe96c3ca8e1f9c, 0x9f1801b491230693, 0x39e28db8625fd091, 0x9fab50355dd44c8e, 0x145155da729b280d
        , 0xd3ccf8101d4d76d5, 0x5a0faa1a8c2b6c68, 0x3cc66c84cb54ea8a, 0x51052ce3f566c773, 0x3bee14de65ae9ff5, 0x7586118a01ccf024, 0x089e791c896bf15e, 0x35ff022d261d93d6, 0xcd3ce13d8f7d1cf9, 0x4f1de98f95b7b8f6, 0x51e68a2462dc41b4, 0x61ad9e3c23f6dd29
        , 0x584fea6480ebdb51, 0x5d52fe073f9decf3, 0x9afe483eadf336d5, 0x1dfa03c980b1696a, 0x55f73d47ff819a19, 0x697bf55d361100ed, 0xded4804446399419, 0x618c94467fce259f, 0xf2597ff1f08ef50c, 0x07c935b98dd933c0, 0xbb758cbc78ded5f6, 0x1e9a0d06af13148f
        , 0x879ce1457f4cd4db, 0x28396ca1962d4994, 0xf5095a3dc57605c3, 0x1e570f3da4c527b1, 0x2af69a3904935787, 0x591ee376fdd01cce, 0xf77b58df88bc8633, 0x5464d651b2f395d1, 0xafbc096b1e9a86ae, 0x6ce2df4bf65b6b28, 0x3b3a828d2e9d3e08, 0x6382011d8d2d66d0
        , 0x94987ca64d3d193d, 0x50ddf70d3b6d56af, 0x8d5df67cc8ad15a9, 0x39208098bc5b1f92, 0xce99f520dfd5a4fb, 0x323bbc87b86a7ba9, 0xe13f88a8d803c789, 0x56ffdcbdf2200055, 0x3aff0da31b24c72d, 0x70011566460c0c16, 0x76f7b7f53ac46a13, 0x1c069bfeb7077bc2
        , 0x8f47193ca14a3c36, 0x6d73e34af088de3d, 0x634b2bd9317d6634, 0x5b404738b77f1ec8, 0xf34fabb71ca1cb1d, 0x054abbcaca546a46, 0xe8cdcadd08eda660, 0x6971abbf958bdef1, 0x41338557dddb4eaf, 0x1e158585b079b67c, 0xd2270474cfa26068, 0x53b36d32b3cea469
        , 0x011523c16c543d08, 0x4668e92c5f73314e, 0xbaef3ebe4117acd1, 0x04037d1aa713931a, 0x68e118e4e390c68d, 0x6b80cd55a44c1575, 0x7307ea8a5729c032, 0x5cc5475feee99ab2, 0x34450e424c14ac75, 0x3f09157e5db3dcd8, 0x62ce2b1b50588052, 0x27a899c54e652f8f
        , 0x0acd039f2fc2a5ed, 0x4b4044ddd5813eec, 0xc04d189e90a75958, 0x242551bce71d33a1, 0xd95af96b51f87f05, 0x02988820f809d815, 0xb27f65f73b9483c5, 0x2ef60745f4364b43, 0xcb66bdc93f4fb8b9, 0x2b86c9b48756bb8a, 0xf8ebdae09b9867a1, 0x441e70184e6fe9aa
        , 0xfdc2530330cc1289, 0x47d8d65a8b4d6992, 0x8c03b6fa30ae74be, 0x1ca8693cc3bd99d5, 0x699eb1511018f2a6, 0x3da04764d9f4fff5, 0x361720433d3aab59, 0x2fa911612cb857ff, 0xa4057da10c2f1cac, 0x48a219b933a5c619, 0x42341020d15f0bc5, 0x73f8895046a09dad
        , 0x1bad5312c67421b8, 0x4194771b368e622e, 0x8cc71a79e44e0dff, 0x4b4564e45467f1c2, 0x7759f16aafe52093, 0x391b71dcd75fbea9, 0x2a1c0694ab4ef798, 0x023087545444130d, 0x4b7ae1ffcfaa1aa1, 0x64e26f32d73361e7, 0x8da47038bd0b54b9, 0x148cfa6feaecee15
        , 0x3756d4d479c2cc3d, 0x25d44ea8d31543de, 0xd82c8bef26bb2c43, 0x2c2047033d27f37f, 0x5bd33d9837dad260, 0x77943117a3383b7d, 0x12071d697ea583f2, 0x3c7c41272a225bf2, 0x92ebbdfaf1f03ad3, 0x5d61030c68b63704, 0xca6e2853baee75d1, 0x12404b34771a3636
        , 0xbe13c46326667e4f, 0x2bd261916f9be3b0, 0x86e3f8cbadc80f89, 0x74520d8a1794cb48, 0x1e15c745024cf97e, 0x5cee741e1e53eb02, 0x8d088de0af99cda1, 0x625812961cc0862c, 0x4313437321c0e934, 0x60bbc768c424f7a4, 0xaba71fbf3c10e143, 0x37b8ea9f14a915b8
        , 0x8d96ec65c40213ff, 0x74a08828ff77845c, 0xbedb7194daf607a3, 0x17e86671161c8706, 0xaceb98e0524059cf, 0x68552ac494916f09, 0x4cd2971baf1b3c47, 0x68442ebcdde21b70, 0x19629b8c0e867595, 0x6a6955d3635fa47a, 0x6fab45e0f2e393ad, 0x66dd3ef4fcf050c4
        , 0xbb0b7abcfddc7df1, 0x14eb5b751b0bcf9c, 0x1cf79f9ca2fd411d, 0x5c496f73fff0600a, 0x49648d8555426d70, 0x46c1016a2322d8a9, 0xb57fdb870d9b6d4f, 0x609eb65209ddb633, 0xe70f9166bedc82c5, 0x772fb5b5c8afaf27, 0x79a294d9b0227a20, 0x7f75b141112dbc8d
        , 0x98d1c7f88e070020, 0x5953d0aac48217b1, 0xe28253ebe15f33ff, 0x267d1dc11e614c45, 0xbe64f50ab99e2246, 0x4eaaab5c82fe5495, 0x927d5ac07e60bed0, 0x67d3786de6aa1b4d, 0xa71962bf0f6e2945, 0x63d93844a35eea9b, 0xb34228c7d26640ac, 0x169c38d2eb28f5a1
        , 0x4b7972b33439dc22, 0x71478457cdaa1e14, 0x5226e125ec1d58c7, 0x669d8796e78fd4f1, 0x750dd1aaaa44a07f, 0x327c62b55aebbecf, 0x006b8e95b54fbd25, 0x2ab3f95d01eb364e, 0xfcbe5080c0d5e196, 0x2a1b9bd75a57e725, 0x1d2b2b6758139b5d, 0x751cf4af849b7a73
        , 0x164a7d2e337d00a5, 0x00cee3a4cb83a4bc, 0x3498e0366dbe28f9, 0x053d899148d28502, 0x01665d64cab0fb69, 0x4a99132208d68e74, 0xba44bbd4bd3f915d, 0x1d34b0f9172122bb, 0x5d114dc729e8a9f3, 0x08e7a43dd5334b60, 0x28db8e9232f0f3e8, 0x5cb7be1b80264f62
        , 0x9af2c78782508f23, 0x336ae7ccf7e3a1b2, 0x7fe2d4ee2dd194be, 0x573d2e1b2b8a6872, 0x3332ea3363b2ea36, 0x200bc1375b1f4243, 0x65c47c8c06b3260d, 0x42021fca53995c5e, 0x2f7e6cf49bb19946, 0x311fba6a23196d2c, 0xc30c13b62be0d70d, 0x61eeac142711b0dc
        , 0x88526996597d35d4, 0x70169bcbe6bd21d7, 0xa0f1b2d0ad29a510, 0x2ade531472c1b94d, 0x11e320dc189873e7, 0x2d2a1794e85cdb38, 0xa0a8c453a6f621e3, 0x4b06d5b54525f6f7, 0xf42916691848ec1c, 0x1d4216555d578730, 0xf8c60da7290a5b4e, 0x66dd9f39a1f3565f
        , 0x55ac29d937b474a0, 0x4291967a4a369ee4, 0x918dacaa12e6bc89, 0x3d46e8900651c310, 0xaf055430a00e90b1, 0x16f62bf56da5ca39, 0x1a021c33488c51e6, 0x0d64dadf63fbbcd5, 0x0918ece59dbfea7c, 0x3b3319d7dd74203a, 0x1d88545b8b9fa90c, 0x13b792dc908c59e6
        , 0x0a2d939a9c3d0979, 0x321a5dbeb74bf127, 0x5e5947fff66d8470, 0x22ec9ecafd26bc99, 0xde17ca8293b10536, 0x593f56c0559dd846, 0x1148373375485023, 0x23c6b0fdf7448b1c, 0x377904458a27804f, 0x573e91962726ea70, 0x35e1b24f3235ac70, 0x51ba082049f4f85e
        , 0x4bc4918160d47194, 0x5d29a21e3308e1dd, 0x7e15894b3e6e4e33, 0x50dbbd2f4f31d0fb, 0xef248bd235a9c9de, 0x3418add21b634710, 0x96c7233a52363bd2, 0x7c8414ad9a08c99f, 0xbc6acb4a54e6c05c, 0x5729021a1193579a, 0x0627c3e00b08fa1c, 0x3d0b4ff9e17c2a73
        , 0xd507e8755990317f, 0x75b27bb3bc7bfe48, 0x44a80f2c6ce651f5, 0x7b9795fc1b706e46, 0x9de75bdefdf9a640, 0x75ade50ababffaa8, 0xce0ab116870889a0, 0x6f3ddcfcdd59ec6c, 0x6e36833588de0674, 0x291d1129ea28a073, 0xf8b8e53864884d61, 0x706ef8f1ae854d76
        , 0x137a8c6583753069, 0x01e45f1cc620f966, 0xe28e1ff82f76c7ba, 0x36d29eace3e89c54, 0x83379f157f0b49cb, 0x65e9c39e2bacb937, 0x9b323c45070cda3e, 0x16e02f31ab7e2de5, 0x53bcf346635122b7, 0x1fd7e207d6c2de09, 0x3a5f5f94ea1e57ac, 0x0cba06e8d0f0b4df
        , 0x70b440c387a9c392, 0x1e7dc143dee1d800, 0x5498ba6d7239912b, 0x332870a017182d14, 0x6be306fc672d794c, 0x2c2ce211245b2b4e, 0x109b722c8d2ba79f, 0x268520fa9c5f727a, 0x515b300524fe78ee, 0x736201eccbaea698, 0x4608ac113210bf78, 0x32d8fd919c441843
        , 0xc9557e1b04b8f2d8, 0x775437f798dc7459, 0x1200f5585ba417f5, 0x2e00ec5f3e7ad304, 0xfc873d5f2b446288, 0x32270a93624876e4, 0xc646a47c08789b22, 0x2370d9fe925616be, 0x430afa3619e671c4, 0x156468ceac1f5fb2, 0x3b84dec2f2417635, 0x31140e9017c0e58f
        , 0x5c85f88ccb7443fa, 0x0da75f5d64d864ac, 0x295ff44871b0fb84, 0x1b79e10bad3336c3, 0xffdf9942dd2977b3, 0x4c1b198d0f9a1a23, 0xba778a24c112864e, 0x74f66897f26d48d0, 0x3fd5c06e867ab611, 0x4b98ce33ff7878b9, 0xf7db4dce75cb9165, 0x11665aa099ec5163
        , 0x2a498f16ae7118b9, 0x265ec3dbb4eb509a, 0x3da4230668ce2c86, 0x36e62baab2e33385, 0x99507d4a79ab4478, 0x25bfb2fc411e8875, 0xd7ac1ec933022ce1, 0x23d341ae033d0466, 0xd295b465e962bc00, 0x23d0211ba2d73180, 0xa03ccd7aff922d4d, 0x1e767148de301514
        , 0xc241ab36a894efab, 0x1c9fc2f343fc1e58, 0xca3b96562bd27a87, 0x53623e2285dd7015, 0x557411f01c219420, 0x19265577096b42f9, 0xd3312d941b23592f, 0x30a9a9a1c3c51c06, 0x3d89b0b3ea6e8f79, 0x7eab751dc5c77cb2, 0xc0a9b186e6df6e36, 0x4f844d583f155694
        , 0x419018232793dffa, 0x2add440b6bd3854d, 0xd55480f131df6e32, 0x318ce3846ae3e417, 0x0565062d1a0984f4, 0x6ebaec63d2bff9f6, 0x77075fe729e79790, 0x0dd9434624c8a4e7, 0xbf8f11e2dfa9b062, 0x1b17d8255ee8b364, 0x62c2150cf72c6344, 0x28106880d081e8dc
        , 0xf4a4af0ddfec91c1, 0x1a8f0e6c977e1f2e, 0x72a7a3a738b9316f, 0x323716728c4e22ec, 0xc14069065ba4af3b, 0x081514248911d367, 0x51bd4afaa8b6c337, 0x50e77a9b513400e7, 0x46c0051b2a822548, 0x024886e41a5edcfc, 0xa06b0efa41cac17f, 0x336a30b01b9c5675
        , 0x74fb2c10ca097626, 0x2b204caa48e90981, 0x6902c952b9a17b74, 0x39c2e9b6b922303b, 0xb9216b9b3c597419, 0x6d92930264f15f76, 0x7b1297d5eeae1427, 0x0f0744adfe1bd307, 0x33b57e265be6a89d, 0x282fa2e533356c10, 0x3a03995c61dc772c, 0x4f5d8f5e893dcff5
        , 0x4bfc927efc48023f, 0x596f2241d6a685ae, 0x3cb3e0afec29b8a2, 0x31018e0d10653842, 0x2fd00fe944575626, 0x1241d8704982e011, 0x970d56664e6781a7, 0x1b05f49d0f3de2ce, 0xa994ffdf63717e66, 0x416374a76ba88e98, 0x8b082ced53f1579a, 0x56781dfab5d2aa4b
        , 0x8151defd1865b318, 0x64669b840d6081f7, 0xe436f4bb5f38e14e, 0x43d438410a974b40, 0x5832ceb3d666be02, 0x06347d9e1ae1828e, 0x6979471b39e3ea86, 0x2cf2cf61cb4b5ae4, 0xb7ab29eada5a6ee4, 0x12e75cb29aca5768, 0xe65b1109d30d1ffc, 0x71f9becd6b320e5a
        , 0xdc8289026647eed9, 0x31d62d050ca5458f, 0xea2bbf523a54c1e5, 0x602bf0b9e3ee5491, 0x25aa73622380ad4b, 0x2b6b1e3271df5f58, 0xdbc5efd86aa0470d, 0x05353c24b8c4354b, 0xa3c7db3cf5e06bca, 0x288a1c8f2b4ea5f7, 0xd6152f5e12ce7ca1, 0x59d4c1b436673c7d
        , 0x1e02554e521fcb95, 0x66d3980f240ad440, 0xabf16f6b39a4d9d1, 0x7fea351ca94c2f62, 0x3d62b6f3389163ba, 0x0fc6b44f2e7895ea, 0xd5c64403cda7c669, 0x2e4099090e603193, 0x9b5c0faf15fa4c2f, 0x46295c9d8e12b639, 0x5ce4add63a5b331b, 0x5fa7bd736c4c5879
        , 0x47b3471447d1aef2, 0x28004c1c22325739, 0xd588437d9a3c5299, 0x2ab19c1812cd27e8, 0x3ae700f680037802, 0x1ad163800b422b36, 0x45b7ef36fabc2139, 0x44bcdeff21dcbd1d, 0x41c6da2171e11c7b, 0x2c35ee79f7c4cc14, 0x4852942759c13849, 0x6492d26f10be050a
        , 0xa6f54e988c50f0d9, 0x6a2db2b6dd62181b, 0xf7d9806b2a5e57a3, 0x57526bdb3ba53d20, 0x17ce6cb1f500e650, 0x05d841b042f8f345, 0xaa800a6c698de970, 0x04f4b559abe2cb8e, 0xc050dfd7259ce49d, 0x213839bdf94db935, 0xb371258655306204, 0x7d323b8b19f9705a
        , 0x26d4502b16b6c618, 0x79717069aa89595b, 0xf867c0e36db41872, 0x13d601d86c76e1d0, 0x2dfc8b0d331b7383, 0x185472f3e42e8075, 0x05bd13e72b10eba0, 0x519a387490f79b95, 0x8d09c1b2d3ad2500, 0x045da45d2cf0f733, 0x640181956862426c, 0x728d57f59bfe1b09
        , 0xf9a99f878da2c585, 0x4fc4831e61dc4e10, 0x6dc602cc54394fe0, 0x0484566b67e9e8ae, 0xc5fcf0474a93809b, 0x71c0c23a58f3e2bb, 0xb400fabe36fe6c43, 0x614c2f3eaee4c0a7, 0x7610a980d0e1c6c1, 0x1ce8197c88885dcc, 0xeade1c9f3ac2cb2b, 0x471ad07baf2f341e
        , 0xd67a837c6b01121b, 0x2a8e64281f59cb59, 0x52e701e42f3262ca, 0x19e0a27dece50580, 0xb5691c17a7bda6ac, 0x43484c311b9df1f2, 0xa68155549bae49ea, 0x43a2c5dda225fae5, 0xfa5e992aed700eef, 0x58911f5623918856, 0x648b81a1e48c4da9, 0x66e6e30cbdd0c3bd
        , 0xf3ba209c169d266b, 0x20f7a86230447685, 0xd1bb5aaa1a0c3d2e, 0x366c29843d1111f1, 0x06c78b642dcc9013, 0x27484a64e109e3fb, 0x8f8eacbca4677464, 0x0b6cb31b1dc24cc1, 0xdf69c84f898f0fa0, 0x2dd426744920f2a2, 0xc0912a197d4c5c69, 0x489ade7f6a98d8d6
        , 0x458769f47f203e28, 0x124f4123fc05ac97, 0x3bb936f4ad6d7d67, 0x330954fed4f00ff8, 0xc2ce650046f90eaf, 0x7bf94762d4f9debd, 0x2e93172a586dfb83, 0x3c7a6062b4113d96, 0x5ddb0397147f0d93, 0x08e3596fc6839034, 0x374e67ff67639bfa, 0x19021c2119888232
        , 0x002f5d04fdd55efa, 0x05b4c6e079e1baa3, 0xe5678ea3ad74c84c, 0x1c42f7826a58a77d, 0xe054668bd2cafacd, 0x237668d3ede4261c, 0xedf46a6374aebb32, 0x31ec8c5931cf0ef4, 0x955c2e95c35b5825, 0x27d8b0ea68259603, 0xb7a8976e427d1ec0, 0x6b6cc5c07152bd13
        , 0x03d88f0ca0b244cd, 0x001cae9a8cfed897, 0xa844b3a1f693a7fd, 0x676c9acb7abdec96, 0x631b6bd5e0cdbd33, 0x29f289dc0cddd9b8, 0x0947d57536fb2eff, 0x1eb2ce650e3eb059, 0x2139b3a40e8bf405, 0x4165edfb39f4ae8d, 0xe061eda67a70d6a6, 0x2e3cc0328c9084f6
        , 0x1ef8329ed056063f, 0x6d4d01ce49e8b3d5, 0x0110c92f1656d34b, 0x6dad1c4e170829e0, 0x584c56c590b477be, 0x597e5f0ad525e935, 0x6008264d8eb7d36d, 0x3f586754999c829e, 0x3d7ea89df5546a1d, 0x41754f7d9a3f4364, 0x3b0796822ef879a7, 0x1ab2779598262872
        , 0xdc37c9f0bbef7923, 0x256ec818ec35a097, 0x4a72da5c09dd5846, 0x51df6c61edcad45c, 0xaef24fcdcf5ce819, 0x0ba6bb959ae689f1, 0xe667bd65a57b3a9e, 0x71ffd591a28a8e4a, 0x06c325fa53a7fadf, 0x6667f2986b2dcf13, 0x3ef751a6d52a09e4, 0x517a104240b8c74a
        , 0xd08cddfd8c8183f5, 0x59237cc71b8147f1, 0xfff94fd188395933, 0x538acc592d10ef67, 0xac51ce386ff0eb1d, 0x69d42b8114c5fe65, 0xa17eda3995bfe8b9, 0x5dc6d98fdf05a341, 0xf2304d375ce8be78, 0x31b58521ecc483ca, 0x04d2d8140780222a, 0x3dc18b2be3ed95c9
        , 0xa48e1639f2d70d2b, 0x4ffd54a6bc0f38d0, 0x8ae3c65ba6b7143b, 0x482eb41f9178fa9d, 0x240b8b4e87ad4f1d, 0x6d8532420059eb40, 0xc135f77e44275132, 0x6261076a0daae349, 0x35316bdb3842765c, 0x246165ba3a8bfd92, 0x1c2d774bd5177a75, 0x045a2f991647e3b6
        , 0xed3b5923594671a8, 0x0514fada5acd4db5, 0xe8297fc358a0f50f, 0x7cd2badcf2952a91, 0x0da45130ea9ac266, 0x26a0d43c1e14c979, 0xbb62b729fe93a390, 0x360357aff7f67ccb, 0x3ad4835d1c7c59e8, 0x570daffd86fa470b, 0xd7c4be698fa3bd96, 0x17e4bdec2ad76ffc
        , 0x43ce4ea9ead7dc51, 0x58ba7ae0d64a518e, 0xe014cc7e64680555, 0x03abc953ce2630b8, 0xa318620c7799be57, 0x2b258fa2e84da952, 0xdd88fdc5063b2ffd, 0x17371dd79a3aa556, 0x927b837578981299, 0x554552101d90ab2d, 0xb45306218ce54bd0, 0x59109b65ffdb6235
        , 0x8663e0c4a180a515, 0x41467fe41c6604f4, 0xae2c1aa4dcb73878, 0x19d3cb02c6c07517, 0xaa147c97ea6745f1, 0x70dac71a31cac43c, 0xb9213ec26af87dfa, 0x67f228e9f60e7b25, 0xbfb59b8cf78df3df, 0x36687792a4256fa3, 0xe1be5c1f23177544, 0x786a9e1b644b1c90
        , 0x4172f47393ca7f5b, 0x62ae5bb4b8aaeb59, 0xbcd9c431fa631b6f, 0x1fbe20b2edc9cc6d, 0x5fdd829fbc0ee085, 0x241dd315adc5dd59, 0xb4b688d625f7dbb6, 0x595a82fee5bed2d4, 0x69653ae0cc11880d, 0x2b9e85fefc402f76, 0xbb2495b507770a81, 0x05d20c575fb34731
        , 0x9d9e623436485ab2, 0x27012a9665f3febb, 0x586cfef484c04ff7, 0x44a5860cc0eabfbe, 0x6fbfe6e2f3532e80, 0x05abeabaaf3220fe, 0x1bed21f2cb809678, 0x2aa62112b7eafed2, 0xe298837cf610190b, 0x1ec8fbbcef9158f8, 0x1efe9b3aa4f96f6b, 0x6a3b842a068b0ef3
        , 0x92dd4b7cd7f827f7, 0x605175bbf3fd1c97, 0x139bb6419c1f6d98, 0x3a3ab2e9978db310, 0xc5c95941c9d5dd0b, 0x34c6c76025b2bce0, 0x0d44115a49bb8126, 0x7622cbeb11daf619, 0x785bff93164ef5ad, 0x7191647d355cb45d, 0x117f255c4cce6e5c, 0x581b448b0e9aae3e
        , 0x54a4f3cb36225414, 0x790180c539bc4685, 0x47064043b7c6b96f, 0x43cccf5b3a2c010b, 0x1dfbf3afc14c3731, 0x1c368f3195572574, 0x00bc2ed3b5070b5a, 0x0332d8dd63b37f60, 0x0744b1908c9bd8f0, 0x2d258e628dacb9ce, 0xbba5b4bdb9c61e14, 0x0bca12295a34e996
        , 0x059c84c66f2175d4, 0x1a3bed438790be78, 0xdf394f577dabb5b0, 0x304777e63b3c33e4, 0x59a29d4fe82c5a6a, 0x72e421d1e88e77a4, 0x69e6230313312959, 0x2da03aad8cf2bbb8, 0x2858d8608fecb0b6, 0x343099e7a40243a6, 0xba29b675d29a8f63, 0x3d2028a4f6f15886
        , 0xf068e2d286047d0a, 0x14999b5d6c770e20, 0xd1874a592385da79, 0x78aeb552c15a1cd9, 0x482dcccc23e9c06e, 0x7b18a19fb54b5745, 0x036c896efe9a7a06, 0x2f2c2ce0d1871c13, 0x3b2d9b9ed65492c7, 0x0649c7e50819d077, 0xcdab66ea7b65e3cb, 0x49b15b40c4aaf03f };

// The table below consists of four mini-tables each generated using window width W = 8.
// Number of point entries = 4 * 2^6 = 256 points, where each point (x,y) is represented using coordinates (x+y,y-x,2*d*t).
// Table size = 256 * 3 * 256 = 24KB
static const unsigned long long DOUBLE_SCALAR_TABLE[3072] = {
        0xe18a34f3a703e631, 0x287460bf1d502b5f, 0xe02e62f7e4f90353, 0x0c3ba0378b86acde, 0x90bf0f98b0937edc, 0x740b7c7824f0c555, 0xb321239123a01366, 0x4ffcf5b93a9557a5, 0x297afccbabda42bb, 0x5948d137556c97c6, 0xa8189a393330684c, 0x0caf2b720a341f27
        , 0x892756b15bcf68c4, 0x5742f77c98a526ba, 0x340a5a1de9f89f9b, 0x14ef680aee75d0f7, 0x84e770e14043a41f, 0x0212c41116c33c95, 0x35b791e6de4dc0e2, 0x5949df08518d5d28, 0x6a0e120744ed10db, 0x5a5183ce844391d3, 0x6f618b158afdba50, 0x2ce2037e470e2088
        , 0x1f49fa149a64ba3c, 0x5f9876d519670451, 0x030105056f55586b, 0x020f1a557d8fd726, 0xdf4cb175b06d86c8, 0x694fbcbe7fe58390, 0x7933294a756a1b67, 0x09dbe9924b58f8ec, 0x590f4403cdf197b6, 0x1c07969fc87a0ba7, 0xc496477712252367, 0x5508976022f1b096
        , 0xefda361e452e1775, 0x7a0a0cccacc838fb, 0xb07e791c0be5dc5f, 0x24d9b6b418cbcb93, 0x497970f3c6117e03, 0x3986a158cb96d595, 0x8f80586ce692612b, 0x305cafda7e4df9d6, 0xc1a1c2e06452914a, 0x7ef989c0eb583079, 0x3a765b1f7364b099, 0x4fee236d58299c6b
        , 0x6f81095f770e8419, 0x53bbd86b7396bc09, 0x2b72ba726b2b4210, 0x625dda1d2901c78b, 0x0ff5bc7b18cd2b3e, 0x0556598c7358d332, 0x0991245f20ff50d7, 0x0e7f58e5e919a97e, 0x5a0561373b758756, 0x6447bc93f87c198a, 0xf9230604c34c7520, 0x6b214425475c1bfa
        , 0xe93de62d6a7f9497, 0x2129459d86f4493c, 0x456394c7c464cfe4, 0x612434fec3f4a1b3, 0x1ed91eddf44261f3, 0x0c6d3854f9e0a3ff, 0xd3fd153188a7e4e3, 0x24691fbdca16910c, 0xbe97465cd7625c9d, 0x2aa61cd373f759f4, 0x824d5763a326d62b, 0x1a0ae39e50da20ba
        , 0x32d0c8481ee4c3b9, 0x6c3687109cdd18c6, 0xe52717142fbf95da, 0x67bfa41fb52ce9c6, 0x4e24d6a088a01474, 0x49a6ca0ae3fb6626, 0xd67f8faa9103191e, 0x674888f5aa6d3062, 0x4ba73824c2e85a99, 0x406b2fd18d35b314, 0xa7087b1bea728ac1, 0x11d2f222317b160e
        , 0xf8946e007e23a469, 0x22a196fabbce31a2, 0x5309ee1bdc1216ba, 0x240fe9953827a324, 0xf9fcb89b63aeb5c7, 0x603b8149ed16b1b0, 0xb1f1876c02cf61fb, 0x4a5e32af612f948b, 0xfc491aede69a8813, 0x1ad9379136e53aa5, 0x5da50db1d5e6c123, 0x2f4014f7fe2c12ca
        , 0xe4f6791d7685c3f5, 0x4c218521c3745a9b, 0x0c0521af98555f97, 0x1462a12953cada7b, 0x0bb2ab63d6452c1b, 0x5783c531ec98bb87, 0x737def53605dbc9c, 0x49f982b930e86719, 0x75b16790cb5211e3, 0x45ad6574cdbae99e, 0x1062b72dfeec9851, 0x45029a09cc468c88
        , 0x532240de77f3a1f2, 0x17bd291eaa9ad0ea, 0xe0a2d7efc2f8a0a0, 0x3a7412052021778e, 0xb0dfb0976acc90df, 0x7fd603b689a7b1f3, 0x1152579ccb00d6c6, 0x6340743b631849a3, 0xebaa47290e0cda01, 0x143265a6d53fef0b, 0x45325d6fd981e75a, 0x0e9780cc39586f2a
        , 0xa4f68d207a8628dd, 0x50d230b51893e841, 0xf3bd769a4bb504b6, 0x55975c063969292e, 0x07727ba25fb8756f, 0x07ff86cf8ed731fd, 0xef57fa40cc35a1f0, 0x70753a70874218fc, 0x615954e2342b973c, 0x5aa9d68f1a59df86, 0x3b8e9e9ff5e44468, 0x2e749114d60a3d23
        , 0x14a1b91ec176db4b, 0x55f91a63d69aae6d, 0xf42382327b1b6d27, 0x2acf1f475facaafd, 0xfd9069b479b58968, 0x3baaf4e5c4a45f77, 0xa2ac9ab98a7aaab6, 0x5466cb5018f50981, 0x3e6ba27771ba3205, 0x31ea90cdea1bbbe4, 0x0000416b5c557393, 0x464cb0415a510d7d
        , 0xd02087d206ff2bbf, 0x2b9c8ecd7fabe736, 0xb2b56d3842caab0d, 0x046ea0b7767700a7, 0x113a7a889e317310, 0x5992a354bef7d0ca, 0x3edda94ed50388bd, 0x052661f767839154, 0x4c28edf6e19e28e0, 0x1d19c2f2d2f644e5, 0x5d732148db35ab3d, 0x680c4714b83580f5
        , 0xa374f282bb80ccec, 0x789e609bc77ae11c, 0x10d2577d599b45f2, 0x1c548b5b857721b1, 0x7baea726b4543fdf, 0x3c1562912d1b4ed2, 0xd6362203b7e82082, 0x1414e523d3c7a900, 0x7ca349951c1d23a9, 0x4da4265e3ce80fb4, 0x7981ebbcaca9ef36, 0x4ebac9e5b5bf980b
        , 0xabd2c1dcf49cb5a4, 0x3f54acfc25c6340f, 0x202eeffabbd11cbd, 0x67216b7cb3695e8c, 0xff7cbcf9b23fc9f1, 0x2eebebdff7fa7afb, 0x71156befa111f85e, 0x1b8fd98df522902c, 0x6b28ebad62519791, 0x6cf0ea960e01d8ed, 0xb4617bc2006967d5, 0x323da065cb3df0ad
        , 0x31687d0741e24d9c, 0x02db8f2b509a7cc2, 0x9243f85924320527, 0x68c360f01d6e6d2b, 0x2351c5e877d5306a, 0x6f56ccfc85c5f3a9, 0x1b09652837c4928f, 0x0b3337554c83f971, 0xe2931be2ccc783ec, 0x46829694ba08c64f, 0x9f35e36358e2c6ac, 0x1474b333b000d170
        , 0x24d792756fc96640, 0x618fda9fef868c5e, 0xb7ff5b125afd9375, 0x778dd97e0440c258, 0xfbff314886219627, 0x3417e1e1e2a7e811, 0x21e959a88f7b7bdc, 0x3508c2eb8c3c8672, 0x827ecdde111c430f, 0x21bcb19fb07aa134, 0xe0c1fa50ab2f5746, 0x401e680b4e6658fa
        , 0x2cc24bab313693cc, 0x20541c12b964447a, 0x374975b6fb81c3cc, 0x52905efb344e17f7, 0x79c5c9b56d8b5f9e, 0x3390bf75d2b9a3ec, 0x7ef3807d895bf4e4, 0x2814165a42046b51, 0x7f8cfd09326fe158, 0x3232fb4f4c9762ec, 0x5678d6dacc194d25, 0x6f7caffb0a7545e8
        , 0xbd981637b23e7963, 0x691d7b7cb88a0ef5, 0x10ba319ae2062914, 0x06fb144f8295a85b, 0x80e620976bf62f8f, 0x2a425971ec73d6b4, 0x800aa9e741d10b1c, 0x230d7d8bd1a0469b, 0x65aace37428dfe8c, 0x0fcab5297f58b667, 0xcf0e9526943af7b8, 0x7d90915b75d4dae7
        , 0x7455a46156259d6b, 0x29bcc06374cce1b5, 0xf2fb0ed3aa87aefd, 0x211a06af0e54dd58, 0x6c0c95c5723de9bc, 0x6299b6ed25008ca7, 0x7fd63e784d4dfb18, 0x2cc93b4d9bc1db30, 0xebc7e2d44c5d13ea, 0x3278e18d4d3d11a0, 0x349e3dd25a215f79, 0x7eb2a7150b30416d
        , 0x05f3d7d5f6a094cb, 0x2a3771d48e331405, 0x08ef39e9dc96f009, 0x012248373a364992, 0xf758f92fc9fd4d33, 0x2339d8c6dfd3ca6c, 0x8b000965962673b4, 0x746ff43eb99d9054, 0x47ecdc054a422eff, 0x33d8f7c8267b7f0c, 0x22fe00ac921a42ae, 0x31e57f3d31fcd8e6
        , 0xbb912315a1c50869, 0x4ac8cdb0fa7ebbaf, 0x0541d74a60973edf, 0x7234900334b2c5d7, 0xf2e545f730adfa33, 0x224e44e63db5ac96, 0xfcba3d005c6fdeb9, 0x2c93a4e6559936b5, 0x7727a0d7ad88d758, 0x2e33100216719cdd, 0x7b2ef89aeb2c0254, 0x1f6de5b74758afb4
        , 0x6ae89047114fb321, 0x3d605e9a6ec6d80d, 0x18e915c727a874d8, 0x699088b5e9d0912f, 0xaf9344618e056f10, 0x1b9169df8245e0b3, 0x5eb8c33d70f4c891, 0x1609ddfb222b13c3, 0x8131c885d1b366ed, 0x7bc3cf9d9cb1a7b0, 0xd297478d2fc93968, 0x13cbb4573a4ea7f5
        , 0xdd37b5cc64d5986b, 0x7ed3d1d7d81ab5dc, 0xac53485f23973c9e, 0x0705675d333b91d7, 0xade5d213c43186c1, 0x6a8bdf57b4bfdf14, 0xa87f88a1de717963, 0x17f29220b519bce2, 0x7af2d7fb0f95c610, 0x28d1d3923b144a7c, 0x8e73c3d8972813e1, 0x00100b40c62e72c1
        , 0x84de7a81fa1f50da, 0x4fa391d6589d8244, 0xbcc3596f0834b285, 0x4d4acbd60a24e9ce, 0x97fa98b8c1835a0d, 0x33abcf8e29901d0b, 0x60a73d1975b3d082, 0x60666aa4325b948d, 0xad54adb769284a39, 0x227a98d113609b28, 0x4a1e1ffcae6a3872, 0x1e4ee44bd67f818c
        , 0x5a74c6bb4387d315, 0x019428c0b1b18795, 0x5cc153e270bbb055, 0x2b3cabdf00dc4a61, 0x834110c026924b57, 0x2d30e985f2d9f217, 0x47116979333389f5, 0x53e3fd6a18202417, 0xb1393cd79c2e5864, 0x58d92935e4112e82, 0x86989a7ec8305b6d, 0x42a8fe4eee28f37a
        , 0x74e212ef01591901, 0x3277917a0397b1b9, 0x7bbcbe6e3d687544, 0x0b8957701d09afb6, 0x6cfbc8ee74503668, 0x48a9925ada9f8348, 0x57045753ba2d0f4e, 0x7d69ca3866223d66, 0xc7054ce22917271f, 0x41bce1e1133b51de, 0x3a3ae42df81ec35e, 0x7eaada0f42d47cc3
        , 0x13b138f1048a57cc, 0x64f98abd7e915a8f, 0x7af195eb16a0c732, 0x11be81a791d634d2, 0x97d8df47430f61b8, 0x0767c7b381271004, 0x3e949136fb940aa6, 0x3bdee340cd956dba, 0xb250ec4ff91d2602, 0x4cde2454d47f59db, 0xaf5e749530d978cb, 0x5a8e2f2119d4d835
        , 0xdf1cb5425a0744df, 0x3d3b08a7bf35d055, 0xc6335e832de4719c, 0x6eb8d97e09154d42, 0x2f6a3f8de3d20dd9, 0x13f23cfd276233da, 0xb4a6b80dfc0fa41c, 0x58d876403acfd7d7, 0x2ad422078b8e139b, 0x73dbee2abbaf494d, 0x09a2758891eca3c8, 0x6ef9a9f1178b0938
        , 0xfc7e9ecb90c637da, 0x3a04345fc10b1a7c, 0xc024e9cb62f9ff1f, 0x6c4f9c3aa4aa33d8, 0x049d6995b95ac1f0, 0x2243845195763a1b, 0xa1466a31700ac276, 0x600fb7123a325905, 0x9d391a64a0d35a24, 0x3b093b550641f108, 0x2275de5bfd2e221f, 0x25f5e7465963db1e
        , 0x3e220107f7e7fb84, 0x6f06a23bc1b85a8e, 0xb4198d19f6eb0e48, 0x5dc11761dad45fda, 0xba303e492ab52a0d, 0x127c69c73da9f528, 0xd3a5b70cf6c790be, 0x0d72b0c50819da5c, 0x193f90d62ec2cdf7, 0x67f7d0cfc4f46daf, 0x7aec083d52f380ea, 0x7c0a1dda4a28bf4d
        , 0x46fd20fe6008cba7, 0x7a588c914115d595, 0x8fb1d3daecf45f78, 0x0851dac094e7b036, 0xcae0a76e2a32a892, 0x104f861322dddb2f, 0xb79d81e46e1f9006, 0x1e4d28d7a2498912, 0xaf3175d3974b89bf, 0x613d00f9a69c55c2, 0x23f6883e8e65226f, 0x072f7ed65c6def05
        , 0x6690e643bb38e243, 0x1a81c4a7c9189b15, 0x1056d1669e4749ae, 0x0137f2a7418f190c, 0xed3192796e699d16, 0x3ed76db45c38a37c, 0x78e86d1475a88243, 0x45985aacc495b16e, 0x47d5c8208e8f1030, 0x6dbe5f68b4d0e782, 0x08d3d0182cf7f26b, 0x64c375ce172fadbd
        , 0xba0f6db3a20c2875, 0x57e1d90a53241250, 0x0315433fddf8e63e, 0x33344750e37dad9b, 0x62cc0d28ae69b016, 0x435fe80f6100d547, 0x5874aea8669d3df5, 0x3b96913f8264d4a9, 0x738067d6bb1314b0, 0x48cccf24cc6f4ccf, 0x6f5e2bbd68b777af, 0x34c2c37ba9635d66
        , 0xd731534900fdbe5b, 0x4e4f9d97afe11d43, 0x81b41214351b73d7, 0x1d48d100ad11a5ae, 0x2a4ee76628e2b151, 0x34902e901877efb8, 0xb5a8561a0fd45394, 0x44317af6d5cd5ac0, 0x354c2469e9068bad, 0x0771fe2761cad022, 0xfda76ee8212d0f2b, 0x76cdeec6d4435495
        , 0x55c98575b3e825fd, 0x2983325ed5d73a1b, 0x563c4c4fb3f466e7, 0x731b0fa413338bb0, 0xdeb519ca57a05240, 0x7a7e909b5c4f7351, 0xefb7c153dd2ab28e, 0x11ca1c865dee30b3, 0x013ca8348d9d7de1, 0x575e0bdaeee8cf9a, 0x464c98a21083af7f, 0x683ddcd85c212ee3
        , 0x1171f0ab4cd02019, 0x22c7e01c7f4d64c8, 0x972ec0ef3f2e2ed3, 0x623f83c2611a476c, 0x99b3f16be9aa25a1, 0x2d3ebc5468990e0b, 0x5d5fba8546a4d5f2, 0x4716e6919d2986e3, 0x3ab2f2bc183f5d6c, 0x5f6257d3910cd4be, 0x341c6f2a78f94f2b, 0x6ee8390b8a5064f5
        , 0x9d8640b9b83ca8e7, 0x033c5ad24466be3d, 0x6f6cd68db30dfd59, 0x52aa6b1c0f90f3f6, 0xfe7bcd4c97403646, 0x11ab3fc960b05fb0, 0x24584b77575896da, 0x427f8deb932da137, 0x928a28cb505306f0, 0x04ae916fe863820e, 0xaabaa98911b9cd3f, 0x59e588ba994d9145
        , 0x9b8f1afabeee9e9f, 0x04ffc7ef3476ff8e, 0xe9cf53ce9937b146, 0x73fe42a801524448, 0x224bda3cf3bbaaad, 0x5fa85056d59884a4, 0x8e6eead48345726b, 0x09230936d41736d2, 0xe679eb58d1ad6be7, 0x08bb759b530b1eaf, 0x9688eb527860e24b, 0x13704d2daf9af278
        , 0xd9273ac71b906f14, 0x57ee05fbbd40deb5, 0xb7788e19ba9e61eb, 0x7967b6dc1c5d9699, 0x36e043fc230127c0, 0x2a716598bb2d519c, 0xc017b2840d4d1b07, 0x1d3bfa489f756a3f, 0x4ad73abf24318d36, 0x1915e6f53e12625d, 0xb219a7c941f89084, 0x2280087a8f4762fc
        , 0x8eb280345fd1b4e7, 0x55b8d4ee5772fd79, 0xc9e63a787e2ce2e1, 0x685741adbda93885, 0xffb830ab11a3b491, 0x7e891121f9356428, 0xc03aea271a629078, 0x71c45932930a2639, 0xe7df192a6bf81795, 0x704aee8f183aadf1, 0x06ddb55a8a7a63d7, 0x52556d8763f3033c
        , 0xb76b458c6f0c33a7, 0x28666b87c362b95a, 0x365ae575a4c27b9b, 0x36ef35110562adfd, 0x89955dd8d927f9c7, 0x526e787d6a586c9e, 0x762e0bc4eff988c1, 0x6c9523b4b5ae4946, 0xe90a909688cfe95f, 0x658a7dc8b3ffada3, 0xbee148ba7a58520f, 0x6819007d8573d1cf
        , 0x75d3b5ec141be9c5, 0x4bc236ae634f3c27, 0x1192fa9b8b30e894, 0x4129d43e1d092cbf, 0xfcac068558bbea45, 0x513e8d87b8116534, 0x5377a179a155ecd4, 0x6c93531e5545572f, 0x727df81ba09aad91, 0x07527139dbc96250, 0x150320b1d8ba172a, 0x2281e85f60a1809b
        , 0x7164b7d524eba6af, 0x50d387163fea4ca8, 0xe90de17d62aebe78, 0x6ab369ba28c0410d, 0x17d07e315a95d138, 0x58b496352453fefd, 0xb87a04dbbc101b92, 0x40a8f0fb757e9b0e, 0x2148b48a696e64d1, 0x4e004a3a350c17d7, 0x17927e9f386b563e, 0x29da9cd441e3e3c5
        , 0x883d2dc357417213, 0x2e94653ff7862644, 0x53a37af548453df1, 0x04475db3c300b93b, 0x2d65fa4d815e7204, 0x231a2db74c2c3ccd, 0x1fd734c0cf4d97cd, 0x32d255c105f6d122, 0xbb74fd9201eb07b0, 0x12e33f1c81ac6f60, 0xfb9a6439bea97072, 0x52e14b7db9cdcbc1
        , 0x637ac1a91ae374cb, 0x1c8622c35adc8224, 0xeb786c50a64b7d33, 0x362823a7232a5893, 0xf22dafca688d472a, 0x18598f0e0237f7c4, 0x97b8497bfff4bcf1, 0x7abf4cb27a9c5b7f, 0xea47c44e3b3d95d3, 0x58728fe3e1827a43, 0x7fd3681a6df902c8, 0x6db1dbbdc413de79
        , 0xbc4effed1ac3007f, 0x7f31a54744887cab, 0xe6559b4f8bd2519a, 0x18a78ec5b0c241db, 0xf6e10285b15d2030, 0x5c1323ea219a8ff4, 0x134b6f20dd116b47, 0x5d0abddbc8998733, 0xa3c993938702e151, 0x0ab6aeb494f6ad5d, 0x8cf3b4beda1815e6, 0x546ce323008c2fdc
        , 0xa10eb5a6a78dbe39, 0x26d2e8a8b8457da4, 0x026ccbe31517d806, 0x2a35174b812f562c, 0x57d70499dd7a374d, 0x3368f951acd3c5e5, 0x490b2515f901062c, 0x316109e7c315c377, 0x32e20eba569535cf, 0x496a8c39d667d709, 0x5578096dc44d5e0f, 0x608a162ce73903b0
        , 0x6b2e65852cb37cab, 0x75b09a2e6ed609a9, 0x7ac84b3082602455, 0x7690cbb594e84b94, 0xfc85dad9511973fb, 0x738a74b08c9006d0, 0x83233fc939d5883e, 0x7fbfc08b5db3c9f4, 0x81a0e493fb5f7749, 0x2c255ef7e69a77c1, 0x234f02e609cc656f, 0x5960cf0b961f3cec
        , 0xac72940237b1f17a, 0x434e038a29d446ac, 0xca6a090e00d8b0c6, 0x1f1aad24001e473e, 0x6d64b6dc133399fe, 0x0899ba41e9dd4607, 0xca590b3f25bbf5df, 0x57217978b0d8ce11, 0xd6b4cb13da6de9ac, 0x3c88520cf564f75d, 0x649fbd5075a7757f, 0x3f2593b90fe72161
        , 0xe1bee53e91dcc9a8, 0x010069dce4c74a92, 0xef83968978aa855c, 0x6cd8848183b53d73, 0x0b3df59610e403eb, 0x713225d446180a7f, 0xcc23112cc59850e2, 0x105796b670a3730c, 0xa147f4ec7a2fa4cf, 0x32da1f072d75b253, 0x4e7007455e85f560, 0x76a5376a771fdd60
        , 0x47eb4fabdcc699f7, 0x4e45db6334c6ed96, 0x36066f2bab72546f, 0x04f48065593ecdec, 0x3fec02793fbb5601, 0x122f74626b64a526, 0x21d0f66ff83b4dbd, 0x1370610ede647f1c, 0x57b82242b88172c9, 0x527dcbadfdc65ade, 0x5e9c9a04385c93f5, 0x64d1cf9e52548a6c
        , 0xba0073337865c994, 0x633ee14e50bcd615, 0xf840228ec4251095, 0x49bb96812a98f08d, 0x82f57d0422f96678, 0x06d7e43bffe7e0e1, 0x33910cca752ae863, 0x04d46e7c66087e38, 0xf14935c4167017c3, 0x3f22e2f44d03c9ac, 0xa6196244f2cd6164, 0x15a2b4ce514fa4db
        , 0x5191a04c4abbd0c4, 0x0e763360ecc8a19d, 0xfef583c184a673c0, 0x75c2f30a7c7433e7, 0xe947a55547c7c099, 0x245c7ae44f6e7a83, 0x67a666f9e6bec2d4, 0x5de0b922fa645ac8, 0xdd9b3e4a5cb72e22, 0x0139c2c857adba8e, 0xa7feb68e863ac231, 0x501381ef88ec2da0
        , 0xb2b8c6a470f40b01, 0x051d65bdb8363062, 0x4ce90414a6d65714, 0x1e510b525d19df0c, 0x569e723f5d374cf6, 0x4bfe02fd38fde1f0, 0xae7459ebc50f9aa2, 0x0f7e2cb170dfde32, 0x3c3da2326a7407cb, 0x0cfc50a85ffd1842, 0x62ab34c85e85c3c8, 0x22b4d9644bb37333
        , 0x57d313b3d87c2d98, 0x4f432c1cba49133f, 0x6163d11fa4befc0c, 0x1ab94e122fddf12e, 0xfb7c9358aefc85a8, 0x5b20068f81d949b1, 0xcf8ed6ff2145c810, 0x5794afc021932d00, 0x5c8987ad9b6e35d5, 0x6bb1f4b836fda03e, 0x794f1fed4a3ea1d7, 0x0cf6d128deb0e7bf
        , 0x54ec3e1c65878cf5, 0x002811763ba2200e, 0x382d917051e77b71, 0x49e00cbd013a9e7f, 0xccf576e9a4cf019c, 0x4b4a66287970333a, 0xf772168915edfc1f, 0x278eb5eca6479685, 0x8a95c8b9cf41cf06, 0x6e58c9c7826d39db, 0x478e119889f2fe75, 0x73ecd21991bd98d4
        , 0x26e751fe9fbb9502, 0x29825b71b0632e95, 0x21668f96ef8bb5c5, 0x2f2a899e53c9a004, 0x2803292ed4345ce8, 0x72731055c7c65dec, 0x3aaaca9c4b6fe9a5, 0x6228d3ceda8bd671, 0x773e2c5effc48eaf, 0x017ab19e0fea9ac9, 0x9609e10496c8d766, 0x121e89f9b302c30f
        , 0x4e87d00a0be96480, 0x09bd8d170ba9dbab, 0xc6756f947ecd4e52, 0x2c9e40bbbccd0f5b, 0x42a5b77669fd812e, 0x66aba9583b080d9e, 0xee55df99d16e77c1, 0x4cc00c5c5eff2509, 0x8c84d5e20ab7c16b, 0x00ae5c96184ffefb, 0xb295e90346dcef54, 0x5d1bda0a39dc3b72
        , 0x75f92d72a89b5ef2, 0x259d998c9ff9ac0e, 0x8a1cfb72a6c433c1, 0x23f5b71d49d67604, 0x478d8f30914f62ef, 0x08fe61135218eca9, 0x4da2ce9bc6488c4a, 0x15f1eafd35283e2e, 0xc2d2be3ebc42ea0f, 0x2a5216539d6ee902, 0xa1e99052e7bdeeb2, 0x3a8f2631ec78290c
        , 0xb71518a82ebfbfe4, 0x24700671c46ebddc, 0x6ef52d591a221f75, 0x4794614db6a67d92, 0x761f5c8ee4bab607, 0x31d9dd8f2361b5d5, 0x1a45593be8db3b29, 0x7f06c365eb116260, 0x9d305a66e52eb65b, 0x5edcfcb5613eac18, 0xef34fd28154adb75, 0x790f805753b9d742
        , 0x6ecd5ac255dfb797, 0x0cbe14db5d9a88db, 0xc1c86c5efa815528, 0x2c636133ba59d887, 0xc75d42c2d9f52297, 0x4bd3540c21e2ebd3, 0x32e7cdf790de6903, 0x1aae3c9837d3e30a, 0xeed028e49d436f09, 0x779ae12351efed1c, 0x6e0145587d9797a5, 0x25156e4cee9a407b
        , 0xac2fd82f2ac57119, 0x7f8c026f1d182ed2, 0xeacc0d8fb3241611, 0x5968db65d2d7545a, 0x7d525846b1121dbe, 0x57949fd7b80339cf, 0x471fe9bec9b66c01, 0x5c270057f1268efa, 0xce092463083f656e, 0x16e8241cdc862cf9, 0xb7cb2bbcaa06b312, 0x3c25936bd8863416
        , 0x19b8ca966c4a3827, 0x1ae43badfd21e63e, 0x1dfd002b95a6ac6a, 0x4708e27f6d98e997, 0xb5fd6322dc31ac7d, 0x53baf4d9a16dd550, 0x025aa2ea5463960c, 0x5b5b33c7a3cfa54f, 0xdba287866ee96b90, 0x4748c1f3f3a6dc4f, 0x2333ec05a80c154b, 0x4a47745d5b99fb96
        , 0x44955b062a6ecded, 0x7791feea9015f170, 0x736bf603d12fc35a, 0x2632adbca5388026, 0x956e4c48e1697c4f, 0x4ee9adfe8600e32d, 0xa584042a0da56406, 0x34a3d7f4bf457353, 0x8d4fd4fe00176fab, 0x15321ee855941f4e, 0x670701ef81f340a4, 0x0c7d7c618aed0ba8
        , 0x73283131d9bfd9d6, 0x34935a39e31bac65, 0x466cfbbcaae8b991, 0x250dd54e18478ac6, 0x659e46c51e40de4f, 0x618ea014fec50e04, 0xfe64d883080b877c, 0x572cabbb6688c4f7, 0xa2c817493a834146, 0x06cd734876378120, 0xe3de0b717336a849, 0x36942f5191db53c4
        , 0xa3f9adf66abf4d88, 0x2a9a144b8087fa96, 0xfe49fefcb78a5b4f, 0x1be40a8616928bab, 0x07a901975521f7aa, 0x1fc66ea683693510, 0x4dbf0084ba42380e, 0x1f374495b918c737, 0xb8346956a380a00a, 0x1346f4766fcdaa07, 0xb4db5689d46312c1, 0x775e7f3274dc1316
        , 0x07898828f32341c0, 0x144390a33b3e86df, 0x70bc604ce1e9c5e4, 0x127652de00220873, 0x2874bc669df50d45, 0x236f4585150161f4, 0x3bfa4ffd318214e2, 0x7cc92a6165059745, 0x2fae0e92090ef72a, 0x26676bd59c4fcc3b, 0x220c030974d1d447, 0x66455887e98686e7
        , 0x4164b8e4d8760ddc, 0x5517a86f840feb63, 0xd9b42c6c9371cade, 0x3a7f03ceecc160b9, 0xdd4086d64cae366c, 0x1b6290c327842533, 0x144efcd2a7a0e82b, 0x16621925ca10d31e, 0xa9dcd13118e208f1, 0x5a90f97edcb1c54e, 0x80c47331c8749d99, 0x6f061a3569a80b55
        , 0x0f6abf619e2a15c5, 0x29106c98122245f4, 0x5860b10985c9b47f, 0x4f379a379e15f410, 0x2dd6f45df68e1678, 0x2c475167ad9b283c, 0x23b7aa00952a6a3a, 0x5532bc26a40c5365, 0xa5c0a8be3596ce22, 0x4fa3127a9aefa56f, 0x944e843aa973e67f, 0x3c7727d45ae87854
        , 0x48fa2ce675117ea4, 0x7bca8e04ad3bbb9c, 0xd57439e4726f88e5, 0x3337d3a6a03b2286, 0xb0b6172902005953, 0x514bd76734e6c0a1, 0xf97f8934eed7c6b4, 0x0abe13cee7f1b75e, 0x6c88107a120e54a7, 0x634f966d7a6e11df, 0x5044c53109b94097, 0x68d49fc65522b73a
        , 0x69e295cd8c444666, 0x542c4c5fd999a224, 0x13ff89418b5da76f, 0x7133fa786a87ecb4, 0x2f180926456402b4, 0x52ddada7931c4dcc, 0x6eaf0d2130c71590, 0x014ec2a2ec231826, 0xac05b61443b34dd6, 0x157acbfab118b219, 0xe4e2f4b84ad01099, 0x0abf4a4da29a0eb8
        , 0x5f852b85b59eab1f, 0x1bd259c4726869ed, 0xce565d9287790a15, 0x17a48442bcf58a00, 0x01e519522381363b, 0x2336d07a710da07a, 0xcfebf2fbdc714cb2, 0x2f7a51474c23b8a9, 0x77db2a07d4e3716c, 0x40e8d8d2d0a09806, 0x644363ce6d401ae4, 0x53f9cae0470172fd
        , 0x58d96ecd8ddadc53, 0x15028204f3d6d696, 0x6f40a09214439ce2, 0x738c5371236c3e56, 0x64f87ee7a28bf9fc, 0x4f1899449a810fee, 0xd0aa95f4bf21e376, 0x6170cc24283856bc, 0x9dfc4927d764ff75, 0x227ea1563fa2e012, 0xaddd3665622ce087, 0x473d3bea07a5285e
        , 0xc0b986ee0d2b0eb2, 0x78e584c740dd18ed, 0xd5adbf30a04fd508, 0x1c6aed5ab59bedbb, 0x25d05fccbddb5ba1, 0x4a58fb6b3f896319, 0xdb2f6343fd8144fa, 0x46a445de6d5b07e5, 0xf67a06684fe9e1da, 0x57b2515923b15c9f, 0x50439940820a2a0c, 0x62f4b9b26f04dab5
        , 0xe79ea601d01b033d, 0x009bc6176f10fffb, 0x333bff2f907ed39a, 0x253d0a9e626dd400, 0x7a9bbedcfcbef06a, 0x2d1b6a7a5b39342d, 0xbadfb462a124cc9a, 0x2e8cde9d82c15cb0, 0x7c3f81bcd6f1b2a1, 0x04cb0b8fa4075294, 0xfa36d3db38cbd304, 0x59fef93442883553
        , 0x91982a741cb9342e, 0x7b9d63ac17b01982, 0x530b4ec25a293ece, 0x611069ad9fa0f0a4, 0x7a262a59b656a79d, 0x6fe6f8f4d6d015b0, 0x2c2fd7641a5d4e50, 0x24b0c507058c911c, 0x834882e492fe45ae, 0x68d0b01b13432761, 0x0eacaaaf94178b8c, 0x123e3a93006d7d01
        , 0xecf2fe69377ff33c, 0x4fc960ab4408584b, 0x2adc445b1ee45654, 0x4989681cd1d09a93, 0x79509599afe9e3b6, 0x7f6ffbbeee861c15, 0x2ed2859fd6391b25, 0x5e8bd52289b6ad27, 0xc949280adbce7c79, 0x510999e865f0cd54, 0x7f957314ce7d373b, 0x4b2c0ea4bab08ef2
        , 0x2d7cc08b5c05a8db, 0x4609a0ea23507697, 0xe204ba35182c55b8, 0x5e4d5903fdef61e6, 0xfe63842f2826598b, 0x782a3fd3ab62a179, 0xd2f01a1979e5a0f3, 0x0fb4c6bdd637fba2, 0xfbff4c192020c350, 0x14859008c3d223c0, 0x65ed7a889c1a2e55, 0x1d78daf483fa12cb
        , 0x5b54d11b01bc09ca, 0x54fde75737306515, 0x89725231105b63a7, 0x712d1f394adcda99, 0xb554006ee9abefab, 0x04dd8f7bbd4c5381, 0x98d22b3a31995549, 0x637a53de6b57122f, 0x8367d69b4c92da63, 0x236f2a9514250df6, 0xb265509af63d7b7c, 0x08522e36bc4b65f8
        , 0xabae725012ce8301, 0x493b257197a98ce9, 0x33185838570e5f0a, 0x65f5477ac414eb6c, 0xd002a36854699753, 0x2be693b4d96efdb3, 0x3b32484119bdc53d, 0x55691ac09a8fae1e, 0x0249e394514c047f, 0x765674c90b78171f, 0x1166f64638d6ab37, 0x746adba4cb52d18f
        , 0x93e293653dda6cda, 0x5d004ed52ebf0b68, 0x65c7c42d0ad96cc2, 0x3350dbe11cafca74, 0xc638cfa8942fef67, 0x0ff2dfffc5ac1164, 0x9e1b625e649aa471, 0x13a219d03d2eb86d, 0xdb92859ebaf9f7f9, 0x645c50918f7d5abc, 0x25c10cfe99f7e5c6, 0x13d858b53f90170d
        , 0xddb258b13ab1e7a6, 0x4849ff49f4e13fc4, 0x9ef87fa85511cda8, 0x48c50d4d3b4d2f7a, 0x6c98422c8007c9ac, 0x3fdd72e65a3d3491, 0x56b18cb165b4ec3b, 0x6e2c6df9e3fc3daa, 0xf6db5aa98ddc97a4, 0x423fd4082f3fb795, 0x42f8f5edf424d0a0, 0x1a091c2696139936
        , 0x3161c2bbb3b2d58a, 0x2e8d339eb0fb9099, 0x45ef7d11f6fab685, 0x7f222a068db3da4b, 0x9af96f9742549a7c, 0x55370df31dcec81c, 0xde98e81b131af02e, 0x58bd0622a474acee, 0x8ab40fa7ca882e0d, 0x5b4db195655f2410, 0x4754eb479ada77fd, 0x67a8a437d6fc8a7d
        , 0x9888254a4f0c9d58, 0x3232ba83bed0c618, 0x587b0de0207b57d9, 0x020df6becb096aa7, 0xef9e41052a29a8ab, 0x4ae671ee70a15a69, 0x167ce954923ee086, 0x6878c3996c1de887, 0xb29c711490ac097e, 0x1cf41a9c2577d144, 0x0590796ba46d8d29, 0x1c2e6dc8d4aebb65
        , 0xbfb904f8ac9b4cb9, 0x4ea1742c786469e7, 0x5a422f48401be57d, 0x0be0afdc77d6d32f, 0x5e8765cba2c738d3, 0x7dad0475059a089d, 0x9288ae0c40df7df6, 0x51c65f97715a16d5, 0xa9615d4c786ff9d4, 0x507ffe03ec0189ef, 0x1c1f46684604e41f, 0x282fe9d567db0efc
        , 0xebee7f8381fb8178, 0x5bd4b6045c208d57, 0xf35694743439ed71, 0x7cddd5a373ebc5ec, 0xa58df33cc68e3b5f, 0x40e6714f5c5c8df3, 0xea881d4bfd489131, 0x6b36400b491c28c1, 0xd4475cf594b6303b, 0x5b630cddc72e654a, 0xa0b587ad34394ce3, 0x3ea3ba6014f86275
        , 0xc3deac125d20eeee, 0x2ef3568410a2b3bb, 0xee6ba3fac5d7ec00, 0x5fabcb3337aaa23c, 0x6b1212e7b817889a, 0x0b37d285a9be51d1, 0x617ca543d762bf51, 0x0896b4ca694b01d0, 0xe3add9718277a1fb, 0x553dee7dd4784865, 0x904b8f7e936cf430, 0x5b6a78f20b244b90
        , 0xa2b876c2914b9bfa, 0x704de952e9d969f4, 0xb04ea1b54b7e7654, 0x5d307bb3949cf660, 0xcee4c23ebd049d17, 0x7a88293bb1031063, 0x00b8432b8286f656, 0x260a9c86a16216e5, 0xd140e6e6629d8686, 0x296011ff5601a000, 0x536f0f76cd9b2928, 0x267409c23a823dd4
        , 0x0f041043797f8423, 0x3da6102605962ca9, 0x2e69dfeea02098ea, 0x427e7eeeecd3a0c5, 0x75efa5e8a590793d, 0x1f5841df6dfdfc91, 0x1aa1e1b8b9f3c326, 0x07bd5b0983fcee91, 0xd169420be9c48939, 0x7940334f0bb9023d, 0x9bb330fff113764f, 0x674ff1b0cfe246c7
        , 0xe2083f8d7129cbab, 0x7e6223e3d9c04904, 0x9be411a7d5e883a3, 0x72642664e7c25590, 0xbb1f783b5c412322, 0x46716e8fd737280b, 0xfa363eeaeffde271, 0x6c256c131fc2c3b9, 0x13259abfcb2ce1d8, 0x53b96556e96aa708, 0xfaa7c8d25119da19, 0x05019f438e9f8995
        , 0x05e1d55a9424f1ee, 0x63e8e14e6c2f3f09, 0xe9d844e997a10158, 0x51904ed1e94a0ca5, 0xb09462d4df6bc6cc, 0x2ee5308e62172691, 0x3f8438484547187a, 0x62b92b8d9739ddd4, 0x3ca54ab5d39f083c, 0x25b3336048a288d4, 0x7cab0fd67e296979, 0x58ba2e783962cbb7
        , 0x77808f1a1b8f3515, 0x290c219ee7153bdd, 0x7584441f79128f01, 0x0442db406f5135e3, 0xe741de52ec030a9d, 0x37469756586776b2, 0xbd64c2a7173adde0, 0x2280b66d20888d0c, 0xdd1b53cb4adb0fb2, 0x3974964394c445be, 0x53b6a95e7c7fdd97, 0x6eacdc6f50496d95
        , 0x178d04c0578a5bb3, 0x0d171a5f5215c9c8, 0xfe0d0171c504962e, 0x04eece54b220495e, 0xac4d145001db67aa, 0x6577c466962160af, 0xcddae62d99686ad7, 0x7a053a048d230d89, 0x1ff09aa0e605a880, 0x5d260426f355232f, 0xfbdaf7b0b53aab89, 0x5eef31b9eb0df78c
        , 0xfb787e56b7276288, 0x4dcccba87d630d06, 0x415e4a4bc0a44b01, 0x0f0a981f71d8ae33, 0xe0ebb786f98a1502, 0x0ea4aa3ce70dc628, 0x8d36240617ebe037, 0x2d20c0e1d2002b5b, 0x336f8aa411a30282, 0x1d87c67d8178ec4c, 0xe468dff8ac26b63b, 0x266086bd7f11c9bc
        , 0x05cfeedc80d829f8, 0x146902a029dd3355, 0x413db9327c068394, 0x55fa413791f64c38, 0xe06395c10021bf9d, 0x18d66268cf79ce45, 0x9e7ae6858dcc21bf, 0x3ad51dbe97b558f7, 0x06792c747aeef43c, 0x27ec9b782170abb7, 0x6aafca394a23e935, 0x18f7cbd98db64112
        , 0x34146ce6b36edbfa, 0x1dcfb4eab7ccea23, 0x68498e1f45b35467, 0x1b20d71a3b71d412, 0x7a875fc94e602e3e, 0x78c15fa449576c2b, 0xb52326d01ccafe8a, 0x3f53f57324d70666, 0x3830836e39bcebaa, 0x27a30c73dd02c884, 0x5dfed73dedf2306f, 0x75ee4a8b6cf54f74
        , 0x97ecc9c5851a8e3e, 0x496b581690c3df2d, 0xf7bba1fe2d169e7d, 0x4b06184810a77bd3, 0x40e6d643b903c7bd, 0x3c90f63b5176906d, 0x92f47e1ac51f1ec6, 0x70c2454c53cc0dcf, 0xb5a75d246c653b4e, 0x7e5173a420a8b0df, 0xcafb44c471d0f4a3, 0x69a3a4e92bbe5977
        , 0x26e93183cdfeb424, 0x1e0489b56fa7e130, 0x669befa672fe9979, 0x0f8aea6a7ef65bf9, 0xff0b883ea96b51ff, 0x31a668763c3c8867, 0x6887a0029701c9be, 0x545644cd70c87d63, 0x537b6fb7db9410e0, 0x6ca227f10229b3b9, 0xc7d1b4d71ff22468, 0x522058d3b20569f9
        , 0x5f4bfd813a51fb62, 0x105b94a3a42424a1, 0x96dfdb685825857b, 0x14d98588154500bf, 0xb4db83514c7a9404, 0x67aaf998856faf37, 0x1229d7e95dbc821c, 0x7e617a17a2f72bd3, 0xe964cdba7222695a, 0x677619cc40a07eaf, 0x7f82c099a8df7538, 0x2a219175ec95a1ad
        , 0x755ac147b51ff3dc, 0x4a87f652f86823ec, 0x6d8d4a923f50278d, 0x4bb952ac98c0120a, 0x968c57a6a31e482c, 0x0855a11481fd5653, 0x3f05db6ac608d16d, 0x33f9e5746e1079c6, 0x1f3458e3ec51f53a, 0x4ae3fc836ceccf81, 0x3c0b2e2db5875ddf, 0x42336a1262cbb5e0
        , 0xe3651453cadc3868, 0x25081cfd6e80a2de, 0xd4cb31092872e53a, 0x16ca9349a11a9c37, 0xb1d3ae440d1cb675, 0x41b2d6ecbccbd6a4, 0x475e6a844c3d0ca1, 0x2cd0e0dedbf07023, 0x85ad446ddb002a6e, 0x72a06e5419a64609, 0x9e779387e9a3276c, 0x414a8163a9408b10
        , 0x25c7b53c1791333e, 0x3ea57190b42cd838, 0xbf20b346b094f121, 0x47570cba99b06c9d, 0xe6bd01c8746cb5f2, 0x3c0b0b8c4c0968ef, 0xb22009690e243975, 0x251737e4a5643da2, 0x3cdd49123ab89dea, 0x68748cd1e3cc45a6, 0x563746685effea7b, 0x4e4c5b1c86eb3a29
        , 0xe1ba017516d32070, 0x5cdd35a0c4ba93a3, 0xdbc66a0c7de30288, 0x22107156a0f700f1, 0x0fb69045aac0f647, 0x111dcb9763d08bc0, 0x266db39f6d78cced, 0x02a32587c7033892, 0x76fc94ce6a2a4b19, 0x474db0f12fcfa96f, 0x0c44584c08377ac7, 0x5f435bf43140f4c0
        , 0xb9741c3014eef7a3, 0x54596c23b536ff04, 0xeadf56bb6ea39450, 0x32f24f6e1a656b10, 0x21422e4dd5f54e3f, 0x0d6ad57853660607, 0xf6f62ffdd0bf9928, 0x72569c930015caa7, 0xf4293579931b9216, 0x049d6a4057e6827e, 0x6223e20060be0e05, 0x20d91ae969dfa9a4
        , 0x02611b345456d47a, 0x601dd413d1bdea0f, 0xe6b017b26bbc9bf8, 0x63399ff3d6542359, 0xdbdfe225045a9764, 0x10acd93346649beb, 0xc652d5a50e0535ce, 0x49efbd5639c4caf1, 0x65a5dbd8a304de65, 0x08ddebed0e865be8, 0x5db8337d5e715261, 0x34cf4c75496807e2
        , 0xd840c7416e44b56a, 0x10fd30d282d8b151, 0x36ffe6df2c1c9568, 0x66d8a38b6d31a2b1, 0x01fad3aa61984774, 0x412a9fd87b303d90, 0x2720945ee0f0ec9e, 0x0c91b4c7ea84cf37, 0x98462f25fd5832f0, 0x6f4cd578c490d842, 0xecc7d24c31ed3342, 0x580ab96994515fd8
        , 0x6d8a97ed98465b3e, 0x16995dc010908ae3, 0x50626a4e555b774a, 0x082636e5a8a9b568, 0xa99435cc4823b413, 0x41fc423d10eff4e7, 0x114236dce6f9f9dd, 0x6c3995c4bbe0aadc, 0xf3f22c975935753d, 0x6b1b3f27edec2a78, 0xdbadaac32ccc292e, 0x3856036f8a3795aa
        , 0x947154caaec01d73, 0x0a22e573e3f0f49b, 0xc50c949f39c184a3, 0x2aadd0868535d0c8, 0x22bc5bbe5f992446, 0x15d36adfca3ace90, 0x038010e37a6308f9, 0x161b06d8d7180307, 0xcfbf4e3abef8d056, 0x2a1765fe9c7696ba, 0x6a15d44ce18ef392, 0x5405239c0369de64
        , 0x5fabda1210f58e29, 0x40cbb03974b37035, 0xa29fdf2875322520, 0x3b32ace85edac547, 0x0f0c92b41d679df8, 0x7f07ecd47a7d2f0c, 0xb5fc65c05accc95a, 0x0e8b1da70636f221, 0xb2ebd131f4e8a846, 0x7df51e4aba57f391, 0xaa2f3d40fef689ed, 0x0ee1e115fde5d582
        , 0xf7d025b42e240ae6, 0x29fc1befeb526af2, 0x7c5ffcaff205e565, 0x4cf4d0d8840e2e1e, 0xb8b00d1810ad0ff6, 0x44d3af686ba915ff, 0x86a8fd1eeea8d08c, 0x3eb300adcf6edc4f, 0x8db03c266b588186, 0x289d0fd301e96881, 0xba83ba260cccc170, 0x26ee69546ceb0c77
        , 0x1109d8bf92c4ea05, 0x033aa036671937d1, 0x4bd9902e5a664a0b, 0x42bd48ed44fdbb71, 0x7359e19357a9622d, 0x0d6ee92855dae22f, 0xc24debb323643859, 0x4c60fee1e191766e, 0x3beaec0e99faa328, 0x056c2ae1709c5b0a, 0x7fe89e0c62710909, 0x7e3b5cd3ac4e6ce1
        , 0xe9d06486ac7370a4, 0x4b1a8c62e99f9429, 0xb11a50e20bc3197f, 0x75ec513c25dac300, 0xfb9fd064b1466dca, 0x290379cfce59308c, 0xca3ee3fb7db99943, 0x2af7a3e930faea44, 0x0d294e6d1505e35b, 0x7d534585181e001f, 0x90285700831d4cfe, 0x419f25105d06c90e
        , 0x5f71e79f5f828172, 0x02921e2a43326798, 0xa0981553e84d4a6a, 0x220c82041938573d, 0xfd2b5b78ef20c927, 0x3c99a2dc611caddb, 0xfb1247fd99ed2828, 0x4b3a3739f724890c, 0x7775ea2d7d2d1017, 0x3ab07cb5ba8ac987, 0x82e5123a20a6b5c3, 0x44965098aa82161f
        , 0x20948c77e9ac4c0c, 0x521e934ab214157d, 0xc8f4f4052dffedab, 0x1da963c2ef46f27f, 0x3be7631e212fa2e0, 0x0d188e88d1a4184e, 0xb4483ed385de4bae, 0x4ffadfde83d2b0d9, 0xacebd9a51a938608, 0x40968c0c9302b0e8, 0x85704404d06f3a5d, 0x3e9f477a61a26d37
        , 0x1da1efc7cbd18d12, 0x4fb87a47b9f2cb04, 0x7556a45e8b5c8caf, 0x7f6991b7723b35cc, 0x3fa10a169532635f, 0x15e61b1cd72bd52f, 0xe6b45dc3b4667c21, 0x45cf3bd4bbf39baf, 0x7343b0636a9d63f9, 0x457551c49ac49567, 0x331e611a3fcec018, 0x7d19e2584756b92d
        , 0x78951df174059655, 0x0573cd896a793337, 0xb3e37121fd458870, 0x3cc032b1a1bebc3c, 0x2571dd06d24d5a41, 0x017382ec4aa29ffa, 0x6cda850c15a224ed, 0x6af59bee2d7586d4, 0x287d3c4027f80ee9, 0x6aa570b9e51d4f25, 0xf29f327c5e0490d5, 0x00fb62f93f43edfb
        , 0x7b06e602dc313277, 0x5d8dc98e723b039e, 0x5bb61813041a589a, 0x2a4c9f13eef7f1ec, 0x9439edcb4bbaba6f, 0x027f4d494e7784ad, 0x087ae2a2fd6bbc8d, 0x230f37ba41aec2ff, 0x63876e43daaac09c, 0x28abd7ae6e17dbe3, 0xd354d50cf000982a, 0x1dd774a1273aea75
        , 0x243658930d4b0902, 0x0df50723a2da63d7, 0x22bc07b9ac9628c5, 0x134123d68aa939cc, 0x4e84ee2cf0d450e2, 0x53a8c6dbd4aa9ed1, 0xd06e741c45610565, 0x608da7f96f2f7e19, 0x59b7fc9fe6a0243c, 0x0da36bb46fd1eb3d, 0x09a11de836914182, 0x3becc1cc0b96f1e4
        , 0x820b8a4cad71c17f, 0x2a425dd0204a843c, 0xf6f7fdaae1523c28, 0x5fb74c0c961e6fb1, 0x0c76e0f72b7845a2, 0x273db117946ce778, 0x7a22d35cdea5934f, 0x73aeeb1b24265d5d, 0x938a618552e4392d, 0x6050215beb6c1923, 0xf32f6ab781efbf2f, 0x2e4ece5c476e1354
        , 0xf2a4a59613812356, 0x555185da018933fd, 0x2fffbf95863bce54, 0x72644f9c3181e7a6, 0x98c6b1d509e3d624, 0x5bddd5730939d7d0, 0xdd197613d550fbad, 0x7671fafa1facb923, 0x13dbb61148c5b802, 0x616bc5c73ccdc3bd, 0x0b175b4c46fd8871, 0x498a1eeb000ab870
        , 0xa49f1ca2d7802521, 0x6906346cce00be5a, 0xf1bc33c727dd52b0, 0x5d005ff3122fd749, 0x51318ad5d7c622e7, 0x50f93d6d15e46e82, 0x88dfa2123ffff3b9, 0x3848e6fce3cac6e5, 0x6cefc31a33ea4f5e, 0x0cc5e7dc4e5e144f, 0xee2009402e59a7e2, 0x257679fdb86f4712
        , 0x4cf68953d8b17e83, 0x710f970c16ce2070, 0x4000b8e9e51e6aad, 0x5af48dacd01f24f6, 0x209679d5d3fcc916, 0x0a3538dd7cbe8232, 0x2d6d7aba44d990d2, 0x46c718f2d4b2c1a6, 0x9953d799a378233c, 0x4f4e80f4a682e7a0, 0x9912f04acbb77eee, 0x317432079a195b2d
        , 0xaccccda6a1c11e3b, 0x3fd895817d0f3be2, 0x016db17673f750ea, 0x635fc619a24009b6, 0xb8447ab3370da1e7, 0x6c893aa19abf4221, 0x5f35ac703d8508d0, 0x13533d324d4adcb5, 0x84610370dece8512, 0x2223f126f9a70f4b, 0x18f00d60f3bf6a04, 0x174bd78b20ef8543
        , 0xeb179bc6a1698189, 0x732bf44a62015302, 0x98352342bc0e4bc6, 0x053f6640c1549e85, 0x65eee8b0397c7ce8, 0x790451f39f2fa27b, 0x36ffa0cb286cdb97, 0x46d07cec4c967bf2, 0x7c849ace30868412, 0x6dee239d339ef499, 0x8ab78548f273e57f, 0x01c5bebd8b7f5ef0
        , 0xe440e5f042eae93b, 0x65583f57fe057db6, 0xe6d5d26c24a565c9, 0x6b3b87a0a6ad702f, 0xd3f5d533117b8e64, 0x4addb9d0da92df89, 0xf1bd51990e0f9bfa, 0x30c624ec1dbcd0a4, 0xafaf2f00da7023a0, 0x3086e132b54574e4, 0x93bdbd4bfd3dd8c7, 0x690976ee132c892e
        , 0x86fc11c79524d198, 0x0f6b95662e02c734, 0x5b78bb385564f568, 0x55c9b3f55d7cd16b, 0xdf1316434ad1c07f, 0x093d67d3fdf312de, 0xa1fd2257ea57b3d6, 0x4b5b18abe4b54439, 0x66c28f5b59d796b2, 0x7baffe6e642fdea4, 0xb9d3753265e68ae4, 0x40903bd6dfb02d6f
        , 0x357958d4d72d6bc8, 0x179330dea4659dd3, 0x5a9ca85bc8721aef, 0x0209f09e03c9b225, 0xc0bf2e9738933495, 0x5e0dde4d715e50c5, 0x2743c96b66a6b951, 0x6af96188a0d6d358, 0xb2f3c72820f2a709, 0x5e9b8fd43327d9a0, 0xf0b13f5324012177, 0x7abdeaf4f741bace
        , 0x6f006249351471f7, 0x3204eb91cfe9ed6c, 0xe09af1c83c13afa2, 0x6d70ed88d5de535b, 0x2078873d1a2faa1f, 0x5c73bedb8d96f3da, 0x41bbb407a3a1ce1d, 0x7a40ec2fb54eea85, 0xd6d569cb9dd722e3, 0x10acf67805927b6a, 0x27c61d818cc0ea05, 0x57b175c9f59904e2
        , 0x4f7b40bc92b5a60d, 0x51431f647b46b89a, 0xcd84dd55cc2a720e, 0x6b36059700809a1c, 0x78e3e5dd060e9a0f, 0x630c0c1a146c77d4, 0xc9925b0dea8fee2b, 0x4728f0604b16a06d, 0xb4601050635b2318, 0x2484f7281864709b, 0xbe2ed2a2523211db, 0x6425d4ff23dd3a5b
        , 0xf0868c09017aef5e, 0x2733d1e1adc6d5ee, 0xa631db49f17f87e9, 0x36d753ced54d5727, 0x451d17fb6c4af537, 0x1dcc4d611dd55b04, 0x0bb8de0c8d3e549b, 0x2fb2ca1271592c3d, 0xd877914ffbc31ced, 0x190809a196504d10, 0x44bdd65a970277e3, 0x13195c678b4b01fa
        , 0xe69a41a54f84d41f, 0x61c7c870565e4508, 0xeca2d2fc6f0e1c9b, 0x7f065480e257152a, 0xfaaa9f7c3a8873b0, 0x43fcdb8db58a324a, 0x969a79026e9da7a2, 0x4eab135af328b9d9, 0xb38aaafe87f85f7c, 0x69eba4fe1a6b6f32, 0x5607f6c6b4d27cbc, 0x273072bea774f9e7
        , 0x3c1149e3c8d51db0, 0x161f8cd433c28bfa, 0x765a61f218fe70da, 0x442b5d405f2036bb, 0x96f790271c564cc1, 0x3d5dbb33505cc956, 0x621a38b446af395c, 0x2da978b45bb70ce6, 0x755aca711da49388, 0x46f2e33e55e86df8, 0xfc5b454d5cb7be24, 0x67df47d68d8f6d12
        , 0x7a1e224893898aad, 0x0400219c89c2d13e, 0x6c969e4d63d460d9, 0x4df64d5df8b60ad2, 0x1feed05a45ff89ed, 0x290c4b59e684b4ef, 0x97ffbc3df096adb6, 0x4ac6037e76561c96, 0x1bc40299115e51b1, 0x7169e0a1d96aa1be, 0x43f55f8b6bac596c, 0x1cc6a0603081a178
        , 0x8e1d2db69bc925d0, 0x6ffb86eed51d2931, 0x3ad1eb242e0af1b5, 0x338198152fcd6d7c, 0xc1f381496df13943, 0x05d9242fe1c60b02, 0x39617510de7eec81, 0x24d8ba5ac76b12b8, 0x280eb2db9e548483, 0x6c51317b3a8a93f0, 0xb2a9f90939bd1235, 0x2da9de86c39f9aa6
        , 0x7f54917103127b97, 0x7be2be5ad3276169, 0xc969d703d31e9da7, 0x0500df3bbb1f8a4e, 0xea05c77685795917, 0x049575a992d09345, 0xd567f8de2daabe35, 0x383fad35a8e035cb, 0xb9353eb2bbd43d56, 0x52b3953221860c5a, 0xf9e4bcd46dbec03e, 0x4b0db0b4a7b3279c
        , 0x8cc5f6b6e1ff80c0, 0x1bd2ce464b552215, 0xd008eb25b39c4236, 0x3b4ce5bb2f42a9fc, 0xe1f249681d153d9d, 0x3e022cb14bc4c5b9, 0x8a11d021c8ed5a53, 0x560d3fb258bec495, 0xf4405852705a6012, 0x5c8bccd2b1b3efd3, 0xd93c0f63ba7ce0c3, 0x337798cb3e93dbba
        , 0x7a9f68cf800c8e88, 0x579afe689f3ebcce, 0x7dd41d6cdfbdb4a9, 0x3802410c4e1b274e, 0x64241d770cf0db02, 0x2f7c8133c74bde23, 0xf3c3fd835ed1952e, 0x741b1d88a3cee37b, 0x74e1ae644683c68f, 0x0c80dd9e0f7a91e1, 0x3984d741f3e47c24, 0x4b3eb97b6a39d252
        , 0x32e9b9410da9a195, 0x11d09fdc04ec3b41, 0xf92fd5e53cddea30, 0x296e095589e0ce05, 0x4e3200c3a283b696, 0x7e33fbba44ecb32c, 0xed3c039790ad0033, 0x5c8ebb260b5ec084, 0xa667455bb79d2e9d, 0x12fbec9d4f5bb155, 0x3aa5f6bb4d0d8d49, 0x0ca652ed7065d80b
        , 0xb7938753d51c6f83, 0x41644ac1a602f9f2, 0x84223d4d63c38f7d, 0x71057b4b8b931282, 0xd39fa015165f47b5, 0x7536c8a19c33c201, 0xbe713ca4166c2dad, 0x456c98c2b4198511, 0x4793f25e1cb44658, 0x1d002f1cfe1a1ba7, 0x9f9ed6e1e1a27957, 0x095dece028426bdb
        , 0xe57d3412fc1001d6, 0x481c63a0d9b25e99, 0xc756b6ba0dc02aa5, 0x24af047d79ed4683, 0xe37ac10133b68275, 0x418b45e570802012, 0x87578def0c3900ce, 0x7c5661923b8c9740, 0x5f4ab0a6fdda7366, 0x0ac6100825e4eb3c, 0x308528e42c9e4d32, 0x436e5979933ddde8
        , 0x0cd6ebe123352222, 0x63d1768a46f33dc7, 0x96cc55dff38c9273, 0x474438da7140411d, 0xa184b89b81cf6402, 0x6bf820a3aa675050, 0x3bd4720417391f0e, 0x3f2b8f859a8e0cba, 0xed952561b125da29, 0x07eb1ac74165097d, 0xc3f70d0c7db0a9fd, 0x5ab896a489294a6c
        , 0xd4b608975c20018d, 0x6243b039f25d0456, 0xf766e98fc24c7464, 0x20035c09d2291e42, 0xcc0e5b5eeb462524, 0x24bcba5505f90657, 0x43a98d98e4fa9bf6, 0x3b621ec4188264d4, 0x633472fe235c812c, 0x31a20844a3316d23, 0x47b80db7d7f5d0bd, 0x22d482f5663780f9
        , 0x4df227dc52142020, 0x25076d0624bf137e, 0xcb4a6ee30a657645, 0x0ce469dbb5ada433, 0xfdb06251f65b9c5b, 0x44f82274a8e8f538, 0x98fa4c81cdec4b97, 0x0ccd61d1abb61d0d, 0xb9dc371344c5ab54, 0x35dcd9ccf8e5f919, 0x67fc81f369ba5722, 0x121b5aa1af6024da
        , 0xe0b1b16b0fb1f1fa, 0x4dc688d6d3b1805b, 0x05c187cf10e40104, 0x71af39c743daacd9, 0xe691e97f82acf4b3, 0x0c46305b9243bf5b, 0xb063af137fde616b, 0x4e26e72a1de067f6, 0x61fe66d01a221004, 0x172fe9240cea50b1, 0x4ff50d37b2effefc, 0x06be02ab0b89aa5d
        , 0xdd4aab96717af213, 0x32322555b58a7ffc, 0x7812aa965889326d, 0x1bd608f60d6457a4, 0x2c7b6b44e999e141, 0x113a86a87856a8a8, 0xd95469fc33814855, 0x4a18dc36f6bfd586, 0x0706b60bdb854fd3, 0x4dc356685650fa90, 0x24ef7cfce41f8dcc, 0x19049c3e632deae8
        , 0x5c9a4e28b7138a89, 0x0f0b7dbc1e5087e2, 0xebf49cdc66a362d2, 0x19e4b815e6576c85, 0x1896051ee3b6063d, 0x09ecc741852a68e4, 0x4009034def986795, 0x36b440ff39b4b5e8, 0x9bc2647ee28af1cb, 0x62613c9dd152b3a8, 0xc2018ae5dfae5f2d, 0x29ce5ef30009c855
        , 0x0b653558b21d2b1c, 0x45e2c505d1f74936, 0x48304373240553d3, 0x0528569885a82310, 0xa90d402e33924181, 0x5e610edc23cb9555, 0x28890ae7e007d28a, 0x7e5132b6b1ebae37, 0x0d5252eb7c94cb1b, 0x308ddaea1fdbb672, 0x99fac0b431730534, 0x77d54ed63b9325b9
        , 0x4d647bcb76c6ec3f, 0x0e968b22ec2cad86, 0x4b22b5ec30b08a35, 0x3b31df3b52326b5c, 0xbe84f638dac3105d, 0x7db085f133ecbed3, 0x7a8b694596f2cf2a, 0x67b2e6c15d16e0aa, 0x4808b20bf173011d, 0x25d5fbbfbe66f864, 0xf67f3f3cd9743987, 0x654250e89617ddf3
        , 0xf5a1a7e0ba0a88c0, 0x3616c781799ab50a, 0x2669c27a2d256902, 0x3a8ec380e12fd7dd, 0xa25361f44a418e30, 0x2942f3001d233645, 0x60f1d3b7535a4133, 0x14deaaa12e5c7bdf, 0x0089fbece10c8d6f, 0x4bf7c313757c803d, 0x65aa30bfbb70567d, 0x4fed47af409a3fb3
        , 0x07557dd875d3daf5, 0x36c49c2380e3c9bb, 0xa21f643d329ae02f, 0x6cf6f7474338bcb0, 0xb5df78136a0f3012, 0x031fb2df2e00e9d4, 0x4d86fccbe75e79cd, 0x23f890e082d03b7d, 0x5716a1ffb50a8262, 0x0199b50aa6cf3302, 0x6a1be351f86090d5, 0x36095efc13349364
        , 0xffe752be8ce46920, 0x65047a340b652f65, 0x320ee55fd03156a6, 0x5af6aa45278409f6, 0xa6caf283b1cf3850, 0x4e3a988f61072f96, 0x750f67926b18f680, 0x09fc3f2927d21a4a, 0x914893c2f2ce1169, 0x4d15b367121b3e75, 0x6cb12559723774f2, 0x3ee5b8c2a70e054a
        , 0x7dd9b3518d84d2d7, 0x147d5a5a53f57a58, 0xe1bd0904ad842a05, 0x3a0f3b029c9a5845, 0x7153c03261410074, 0x4e203d6737058c17, 0xebecf5cb79f28af9, 0x574b889870c279f4, 0x326317b005f444a4, 0x7480da44b34f4b1e, 0x7c5f21cdc46275b2, 0x210494b9ee24e4e0
        , 0x3cbf6ca1f4aa4ead, 0x6bf3872ccbfed940, 0x19e8a84673a566ca, 0x61a80e16990401a2, 0xea2e029e7f9b3824, 0x5762298465f0ebd3, 0xf60e36d4969f9af0, 0x00b826180531c799, 0x17120ec95cf3c61d, 0x47196cd6de85c7d0, 0xb0d47cff46a5cba3, 0x29271400d7ede26b
        , 0x835908353516b894, 0x4bc57f8c1eedec8e, 0x2ec5deede5c0db5f, 0x7b9fc48ac4a689fb, 0xf82ce6de88fc10e5, 0x6c5d84a70e03a3d6, 0x88a211fc4ea531f9, 0x7d5583e5918aa03e, 0xbdf2d70766fb8f39, 0x5926497e734ab18a, 0xd6a9872b800cacb4, 0x757c1cd521fd22d6
        , 0x22d50b0c13ec4bc0, 0x288a77d34a15e99a, 0x95c8e78fced3d4eb, 0x45ece109c15be169, 0x878ef262d0132128, 0x48110e9fd98939d6, 0xe3fc5425d2e7741e, 0x050ca6e71f599c65, 0xe02f97605d9fe375, 0x2af48b9bfee410e4, 0xfd34a1c107229a54, 0x43dc6f0cdcbd41fe
        , 0x15b4eb7d65cc562b, 0x369a7b0dd3e91248, 0x2b087611edd32810, 0x116b234ddce09d7f, 0xcdb03cae8e90d2b0, 0x4017d51587566038, 0x081793739242b600, 0x5086e8e633cd52a1, 0xf5ddaee155cb8087, 0x773311b60d59a7e9, 0x36e5aa0acadf2068, 0x7126a4281b192882
        , 0x54a10df54f7ecef8, 0x3cd7d2fbb6e33f67, 0xac31eb6c3e740c25, 0x517db54840feb2de, 0xf17cb269b3ce27a2, 0x04a8fecd1dcc99e7, 0xfc887c1f2f85a2da, 0x280da7425bb55b01, 0xa1af72f5256a5a53, 0x71da839fc459f465, 0xc203fe7ba6587f71, 0x08a4201f77a4f335
        , 0x6cb9ea5683014d96, 0x5da17076b6b51ae2, 0xb55ac168c3e3997f, 0x41b9a32373d78f7a, 0x96f58033b8600a50, 0x6ebfba3ec9d956cc, 0x0ff8883707d66d0c, 0x2f562b035445226f, 0x2388fc015bd368c7, 0x2b7d802ce27f627e, 0x301f0369c24083a6, 0x77e139f6da8d5aaa
        , 0x9f78574697fce43c, 0x02726c94565421b6, 0x1ad6007338e26585, 0x6134cc5eb35c02ff, 0x77ae739c9cdcd1e1, 0x04e96543233c7a13, 0x97d3926dcded2e10, 0x6bcdff7e14cebb73, 0x9c46ae2b32489774, 0x04a97b9a0473af8d, 0xb0350bd910d9784e, 0x448212d3e2164ad7
        , 0xf3464e0351f5e995, 0x68ab4d24b3ade8d6, 0x86854d534002af20, 0x613f7ffe5de92aeb, 0xb385b4f4608a370a, 0x220dccecbc6f2688, 0xc31ec5384abd3680, 0x25a82841a2000fd8, 0xd19e422504694236, 0x0bc1124d541781f5, 0x0808651edcd99176, 0x41b81f223d429c76
        , 0x1a6dcb2662cc80c6, 0x0b101fb0ef0d1f74, 0x6f02aed8f8327119, 0x5b4c5176ccc4a340, 0x8fcefd200d6ee8ed, 0x0548127287f44749, 0xe1efeca1fadd1341, 0x0e74bc189dc9016c, 0xe90470353f46cb12, 0x69513d3455bc890c, 0x9503686f1f2497d1, 0x280a0bb7733f1086
        , 0x14e5f99930a91dea, 0x7840ad84b03c3878, 0x46e32c654fdbceb1, 0x7e88d2822bb2cecf, 0x4d78a8aed7f8661d, 0x70eb17416ef40180, 0x97b6f1733c474a10, 0x3d0d27fc4c7084ef, 0x730f60f6a1ee0d71, 0x7bf6e3885d3d9302, 0xa1e8af33742f1611, 0x73b798ec129822ed
        , 0x0f669bb094642a70, 0x142927de789fc4a4, 0x0db18e01fa98cbd7, 0x6ae4d37674be1451, 0x7175e98f178b4b74, 0x40534e319bc52c6c, 0xb7211d252c4db879, 0x1a7651f8f3ed1aae, 0x9c9a43932d50cc97, 0x630b232b7201c359, 0x327d77575f5b3839, 0x5f0e19e78431864a
        , 0xbfbb00b6530a3bb6, 0x19ba9d60d97f7857, 0x759779de744bd764, 0x5facbe63177791e1, 0xc74ea511c56a3b61, 0x1d8909e84083c31d, 0xcd20094b507af492, 0x2ef1b9c07c92ab37, 0x8430ed9ef8494fc9, 0x3f9170e6df5b1fa1, 0x1fb8dbc837175d73, 0x65b961b58008d022
        , 0x7e1afb6816864b6f, 0x54c4b92c534871e9, 0xc0a1dcd60d61ef84, 0x4390f0e992c41298, 0x1e54e2c8b7c27348, 0x7a987e01a2ec308c, 0xee42fbd90c4a89fc, 0x1ed8c77f8d7c609d, 0x569dedaca99a3346, 0x0eb471e609fef4ed, 0xc915522a3b9fd03c, 0x726453b246746bfb
        , 0x4ed3cae53dc5fa4b, 0x1bf1e4b34b9feef6, 0x0850df9f0401fac3, 0x0a58d33cb2422e2f, 0x3d197f9603ecfc29, 0x45e46edba1cc432e, 0x96c0c93310d9bcaf, 0x18de3a458be2c33f, 0xc9e65e5bcc12a49a, 0x71a5345f0239b187, 0x53b3b2f01c5710b3, 0x438350f57ce2ec4a
        , 0xdbbd368a760391db, 0x4033638dfec29fe2, 0x297ad75ed73117fd, 0x269c08d54b106e8c, 0xa4e3e4fd238b4218, 0x1f48a1cb09208aaa, 0x9575153115cf5fa7, 0x59feeff0876fb74a, 0xfdedb4af6f368710, 0x79be1fe79fa674d4, 0x689d6bbb4c707c39, 0x394a451499057bb1
        , 0x5887d4fb21fc43b3, 0x37628dfc4b5c23bf, 0xc66b76944b34bd13, 0x6e97f0a8a45bcb36, 0x3ac6b10139edbbdd, 0x313f4846b6745833, 0xf8758d9777cd9037, 0x02fdc98f02692537, 0x9e79f381fff833a5, 0x25ac5d68c49b105c, 0x1e9f48a076d8c9ee, 0x788c85c9fe9543b3
        , 0x776ea51db3b3b778, 0x0007c44055b64db2, 0x3c392c2a82fddd25, 0x65000203be8ee976, 0xea119666ab7c50ab, 0x528b2700e8f82d39, 0xc4aaf797118b8282, 0x55e5a7d5382e0d3a, 0x15a80b22e89f1039, 0x199f68594b1247a0, 0x8d5630750d622435, 0x2687f48cc6def5b2
        , 0xa16b0c0259eafaee, 0x7aeb10834e93595a, 0xe31bcf34ce679d9f, 0x4e2c19829eee3c87, 0xa46869cb8ca35c9d, 0x3cd35313c08504eb, 0xa088eca66e98389c, 0x44c562f0f7262740, 0xd3eb8a28f447523a, 0x43a0e059bfe37576, 0x0312c5d6d0f2e0ad, 0x5f30aaf0d1614c61
        , 0x6f09a7a6e182b0aa, 0x575db3d21a82296b, 0x6599bb5eee7925e6, 0x093f89458dcc2fe3, 0x70c4af785151fc84, 0x1230c0c519de5480, 0x0e66f8f93075a4f6, 0x5de4a122633a5c6d, 0xdb99cf83f9ece1b6, 0x1c3acd4a13ded617, 0x4dfe69e68f59c447, 0x482ba1f7715a3c16
        , 0xefeed2a7c81ea8fd, 0x4e089eeb713a572f, 0x78bc74acfbdf322b, 0x4b4951ce8eb86fbf, 0x0eafb6b46ac6714d, 0x72913ed109f7d404, 0xb498bf6fcde9e3a2, 0x3c08a283ef5ded62, 0x9af09f593a48b346, 0x7ed52441d00d4980, 0xa78e843ee5df44ac, 0x25db12d420a86151
        , 0xec840e7e89d049e0, 0x5a34cbe928bf96cc, 0xd875dc5525da882c, 0x2af4442fc256827d, 0x089fb428c2ef5a5d, 0x0b573ace080a3d9c, 0x6f57282554c240da, 0x425ceda6707b6bc9, 0x94b5a8c3dde824fb, 0x264f6f6a445b5da9, 0xadf292191c5c1eb7, 0x5e302e82fa4e5533
        , 0xf51712fc44237f35, 0x2b0af62c42e56e66, 0x10392cb4d9c71b75, 0x4d7e08fe8457a95b, 0x210b9eceb04534bf, 0x73329d1c7d88e1e5, 0x667a43fdb4ba79e9, 0x3435ec04276ede87, 0x38b8540a1a78b098, 0x4f6c266e6793bb78, 0x447ea35172754041, 0x109d7b742d8c3dac
        , 0xe3ccab45d2a4f6f7, 0x59040bb73f3bbd2a, 0x730b39d65645bab5, 0x5c61aed2f83382aa, 0xa992143de3cf83e1, 0x13455cb889b700f9, 0x54648228b310e2f7, 0x5b837752ee0f733a, 0x3923a6c0e5ea0dd9, 0x5ebebd01fc9ca9a2, 0xa34c205b8fd94258, 0x7d1a10029a0b6cd5
        , 0x6c83c02241a46527, 0x4127c85d6be1fc62, 0x26f86ff5ca7240b6, 0x2167391e7dd95cd9, 0x79227506ac78caef, 0x1a2cf919b8832a0f, 0x07745266405cf574, 0x38095a07f5713ae1, 0xe5eeab985ca3e7e7, 0x6a5dd9eeb734d639, 0x991027ebe44a4822, 0x311085fb4de9c1f0
        , 0x33f361e21066c3b5, 0x550091d2dfc8688f, 0x376345c5532bac13, 0x0aa0898f990931b5, 0xea2f3346e5d3226e, 0x208790ab78776afc, 0xac7c2ae63433850c, 0x3c5c373ada10ef52, 0x96c1b4003f4cde6a, 0x4546a9c475c09781, 0x6c961fd3e8536294, 0x43f36e63fc0d5066
        , 0x296601d8c42167f4, 0x241c1fc38565471b, 0xdb00a27e11ce9617, 0x60381181b7e7e4ee, 0xc1076b7635ac4d52, 0x0166010ffb8dda38, 0x5238f69becc43e0b, 0x63303a2015708b17, 0xe8badb2e5bb22591, 0x3a10a4e218b6131d, 0x236ab01aabf1a7b3, 0x1ce8a51a68a4126f
        , 0x59e775e2a2a87928, 0x770b48eb4b738301, 0x0b43c2be176bf79b, 0x1957850fb6424660, 0x44455ee1ecb0ab2a, 0x620ceaa116eef4f0, 0x0198f62cb6183f6b, 0x3274f78eaf2d55db, 0xd2ba4e460cf7ed5f, 0x19cfc17bc0b66f43, 0xcbae6f45b1942722, 0x5d93e44739147b58
        , 0xd07180b9d28fc597, 0x35372b21b2ea5a46, 0xed2673477f083464, 0x7a9ebeeecc57e6c2, 0xb51d991a81a6b314, 0x35e7d90f4ed6de58, 0x45f21e209510dd05, 0x446ffd2715c8d380, 0xe69b5c7a9b6d3e76, 0x1379e79fb96912e6, 0xc161c848bd508738, 0x22264a049d8cfff6
        , 0x32321a68ff7ef7b3, 0x57b0e50cc585b333, 0x1c08c65ba9d764e7, 0x5534c793f92f00f5, 0x7a1ced97eafe6fe4, 0x6b8933739202599c, 0x618c5f8fcadd3ff2, 0x2a8719b3e6548653, 0x346a9ec5c4200f0c, 0x7a36b8d00d0eda58, 0x844b22b75021accd, 0x769737059fc5e465
        , 0xdb1ba69b5019f266, 0x1777242305db9ac1, 0x491d11ad264b6ff3, 0x136198dfc57a3053, 0x4a6cc64741eb7176, 0x14e811c97fc97650, 0x6b64667f71be386d, 0x3286fcadf019eb5e, 0x3f2591f4498e10a0, 0x674fa7c32df7867b, 0xbae8ec7ee100dcf2, 0x03b2c0a20a6372a4
        , 0x4c8d76b471e24474, 0x421fb6a7b8a3216b, 0xc672bdb2fe8f514d, 0x202af653d9aff3f5, 0x05e5f80f9626953e, 0x7b721fa3ccd42ffc, 0x99d8e481c0f70479, 0x054c31746d23362b, 0xfbef2e20430e8025, 0x60e1e3f02e7720c2, 0x161701874eb347e3, 0x363924e90cbb77a6
        , 0x180f5ee1863a1a6a, 0x2f79c0046ff79fe2, 0x44679866e35447f0, 0x1c64c6dd73e0d636, 0x1d8175566341469d, 0x5ba634965b8b9e87, 0x8f48744f976952a5, 0x744f28d23db94c8a, 0xd15e84b1f232da34, 0x556f3d7aa38bee8c, 0x14693c56e866ef89, 0x1564fb9a0f81eb03
        , 0xe97eed56fa2b483f, 0x6d3f7e01aebd1957, 0xae8f128aca3b3e45, 0x3d41e85ba2afd3a9, 0xe4fe485e4b6d8328, 0x65c49b4c3e98098e, 0xe96a00e054d6e91a, 0x394a2122738cd006, 0x715cca3dffd90785, 0x7bc3dcde15890965, 0x6dcdc47a33a148ac, 0x435db9d6dbe1bd55
        , 0xd74d4d6e0fd89c27, 0x25e727f6a5380553, 0xbe54127ba6c5189a, 0x65c87d3c3e61939c, 0xc34a6d122a809e2e, 0x7de6b787f097eafa, 0xb8f8b6e701758661, 0x10705fbf97042046, 0x1591614e6da2d44f, 0x7c74f26ec6eb070f, 0x9ad98c1a50249c60, 0x6e1bbd44d64b2302
        , 0x937cee76047790f9, 0x5b4ccbc70beaf690, 0x332e79ae75ae0dae, 0x2e6394161d093556, 0x4b378bf68f6849f0, 0x6c419fa0cebba72d, 0x8bb431e1e273f2a4, 0x357cec80bbe024fd, 0x83a6e913962f11a9, 0x7808df02e2523718, 0xb6690b5dabc49e13, 0x6cef23259375972a
        , 0xd18ac767b5e551fc, 0x5a0ba1dddb15bd36, 0x6f7923de219e3e1f, 0x3ec23588db9b5cfe, 0xa4fc23d42c83bbe0, 0x21581a00768658cd, 0xa295b6e57110218e, 0x3e7bbab1d15f477f, 0x2266c03d3f0d0635, 0x4174f08a95be03b5, 0xaa1a674abb8cbeb8, 0x6bdf6ba553ae3390
        , 0x8a31f824638545e2, 0x2a9e37a0f0eede53, 0x148a53d8cba69f65, 0x64c587e816d96316, 0x777a028a47e97e93, 0x13728e46befb2e0e, 0x13138b44862fa665, 0x0fca8c38a87775f6, 0xcc44bd580dd067fa, 0x40f2f7642e22d02e, 0xab3ba6db80c2f728, 0x5068aa2e2d25b7f9
        , 0x5a8a842c0a2923ff, 0x67c39e8a1006c196, 0x8f5cb9ff55460a84, 0x2e735c20a419a518, 0x0c6ee3fcbfdc2da4, 0x5bf6ed60a87b92bd, 0x5e4ce130e8e1608f, 0x0932ceb3e50028e8, 0x793cf8a0538cbfb8, 0x4e89e2c018beb7bd, 0xcaaa79642f5060de, 0x542a38a4d13f0016
        , 0xa1b0fd9aac663e55, 0x5158bf1f7b33c0e4, 0x060e82f65a4119fe, 0x32347069a1529fc4, 0x5c96ef69127480d5, 0x409a902134df6ffe, 0xdbe8c392eb6c7013, 0x73f2c48b0e3b4a79, 0xddf5060b937e2dff, 0x1534f901278611d9, 0xf47fe29ae4fd49a7, 0x7a2c0bfe75539f29
        , 0x19e04d1b2b0fe7fb, 0x56381ebd8181b50e, 0x5c8970c249df4ac3, 0x08acaece8ede7685, 0xc44f1a71aca0d20b, 0x623edc8d92e4ac3a, 0x5496a7e5885a0c95, 0x20a9ba37315b116e, 0x3765873809f5b55d, 0x23c44c42ebef2ff5, 0x56a96d921f724573, 0x3217815b72b8a9eb
        , 0x2cc1b42f5350a489, 0x31f0b36e85b8c70b, 0x504a5c8c4d2ce34d, 0x1af8ea26b3786eac, 0x69bc5e26d7afd62f, 0x21e399d04247bf9a, 0x6e6d6676a88efb27, 0x476212b9fe9a6fd4, 0x0740fb65284168de, 0x5f7570be65e69408, 0x0166c3279dd81c29, 0x6565489007c4ed6d
        , 0xbafb5bd37b5219c9, 0x00251709f2e210f7, 0x0d22639b51c1198b, 0x0f3c0df3be3de811, 0x3552612be3374eef, 0x0834744318ffa0aa, 0xcb9f1c1e3557a00c, 0x20c359f5de8b6614, 0xd319482a34d05268, 0x42165771b46b75d7, 0xca336c22e8d911a6, 0x4d072f70067a47e1
        , 0x9022c6f101555e9e, 0x4c8c7eaf7cc2d697, 0x629810b2d8044817, 0x25110bc01b06c9c1, 0x1bf9c06bf39eaff7, 0x6cc36f151f52b4e8, 0x76b73a6a14b62068, 0x47dcb0dc89db3821, 0xfe9dfeac2f670f41, 0x625b5c93b973c417, 0x5f8c917930133c1a, 0x6bd35f3e0992bb2b
        , 0x03b5391a85409e5e, 0x7981d8fd16362767, 0xdb45c80a32a23cb6, 0x67356a7ef48b2dc3, 0x6189236e9f01adaf, 0x07a1e954e5032bd6, 0x53d627199c69727e, 0x25d67e4163cec014, 0x18e7bb6a63a80738, 0x3112be4cb5dcbc74, 0xad9ad6d381643f04, 0x116112cbeabb734d
        , 0x32623abe2d66ff07, 0x4d780300822436de, 0x9bed066c04497808, 0x40db29b39ce86700, 0x6e5e5eb3805602a5, 0x52f227f2b1b9b40d, 0x51c2c4c197a18394, 0x6d8bca423ee270bc, 0xd6e60cfe8fb07f72, 0x7dd66c3970f940c6, 0x66aea7b59a0b17cc, 0x75fcf8b00160d729
        , 0xbedc5ea39b2402b5, 0x0dc3600425feedd5, 0xadc1ddf2cb1b6631, 0x205ee93e3aae976a, 0x7a2cb4e333c98498, 0x7d12eb776d56872c, 0x8e339bc1b41599fe, 0x4600f0a53fac9427, 0x1049d3a372f14304, 0x7b54e020b22db742, 0xd567962272a35739, 0x27a1178b1115f0c4
        , 0x6cfb39d619c35e1b, 0x5cb96fd1a9d9d486, 0xaf45cef7fb4fffea, 0x4a73d7b2ba9321d1, 0x44b46b4a80be86ac, 0x2769b50579e8f734, 0xab5d109e7472f372, 0x2bccfba1cbe995b6, 0xc00026115332f6a3, 0x7acb287da1561c53, 0x21555c608cd90dd9, 0x7731d1b2878dae13
        , 0x32122bf5ec1a0649, 0x592b5fa180ec8467, 0x876be1b5ad9ce66f, 0x484c1cc5bb34819d, 0x08e4cc425b30b06c, 0x2766065f0e4d22ce, 0xd90825644987aeff, 0x3a835fcc7fc456a6, 0xf4d801d2cc806d69, 0x41d767ecca55f839, 0xf2dea9fd01f1e74f, 0x74d01b97462211cb
        , 0xe43e280ad29f80cc, 0x5cdf66a69029b231, 0xe8d655a03c862cd9, 0x388e38b58d0e8c79, 0x5d9aaa4848ff83a2, 0x14d6fbee4d6cbe74, 0x0426dcda912109ea, 0x1bb7b9cd75d4b541, 0x3a3c0504b39b8505, 0x35a3c5882b31367a, 0x678793d635a6473a, 0x66abca7e20202034
        , 0x4a90ff1dad300021, 0x18f29036544d2684, 0x2036d39b8f69095d, 0x36490f5645d18cc8, 0x9414d7368ad3562e, 0x7f8108a04558487e, 0x93db0e56d653e40b, 0x03f413ea960537bb, 0x984717b77f7267ef, 0x6c5d9da4a5ee7305, 0x725318dc36060a49, 0x274397f8e79a239e
        , 0xbda7965b4095bab0, 0x6292b2505c7866e3, 0x451fb6a0672d6733, 0x37c560f40242a859, 0x151e56eb818f1423, 0x63451986f0c22ee1, 0x9275ff873a5c75e1, 0x178cdc734a32b96a, 0xff7adbb24244aacc, 0x76518aa0dfd96ddc, 0x161c1c8c81071219, 0x0584d44c10a3e6dc
        , 0x2727282a09e9acab, 0x1298e49c34514ebd, 0x0323d059ca1c0e6d, 0x6072c8b87dd26bc6, 0x36eca2ab28d36f26, 0x2a977cb5aae4ea2a, 0xf157d43a0b9546a7, 0x04d60af0ed661d29, 0x34bc1080126e4402, 0x7677ef9a21589171, 0xbd13797278f07a40, 0x32c0daf0b57f20ac
        , 0xbc83fd1b8366dc2e, 0x6cd07286c4e670ec, 0xf35485a3f339dc8a, 0x6e7e9285f2247e8b, 0xa9d19d3a09943bae, 0x43fa5197eed852a6, 0xf911398a043242fe, 0x4a100dcb1312cbe9, 0xbe2fd86be910a692, 0x614fd829368d7937, 0xdb5a98b1a92d578f, 0x46f1d23e1b0dca7e
        , 0x8bf4c6725e813f36, 0x68bc89078129ce91, 0xff56503ae28f5c7f, 0x2b6e0f4e42178ce5, 0xa97cd947ec65895b, 0x7aa90b66280ff6c9, 0xebbaf32df158a0a0, 0x6a748d0ac02bb713, 0xdf79b5d619e83397, 0x16934947f6485b69, 0xe75185521ab32881, 0x20791e276a7460c9
        , 0xd25c403e22c70bc9, 0x0bf079518e66e1d3, 0x45dd5c971d3711de, 0x66bd2c6a30be232c, 0x607829e5b29e53ca, 0x30ed414e71dc08a2, 0x3fd38589ea0f1d39, 0x5a881a121f37fc5c, 0x27b9394368987a4f, 0x321fe45e13afae2d, 0xc6feb75080f33ea0, 0x02166d52f45eebbd
        , 0x15026a1b0ccd2fc9, 0x1141be93d5bc3d6d, 0xfd20df606fc676c9, 0x4059e26b00ad78c4, 0x0709b409cec6b505, 0x68f020e8acf478e5, 0x875d77d1f5df0cfc, 0x66eb377735162ff1, 0x860482ab417a32ae, 0x21175f47da213935, 0xa07ff0cda099ecdb, 0x26ae5f177ae2b8e7
        , 0xa9a070ea5120eaf7, 0x2581feeba7383f81, 0x49e0f137f1fa2a7a, 0x7fe93c51cfd1ec62, 0x2d74dbdca7777f7e, 0x562da2ba74e823ff, 0x543b4f8609d77a2e, 0x3a0f65212f234ec8, 0xf842e3fea270ebc6, 0x4524322c6a289e11, 0x80815887aa6a8576, 0x46f49d53c3fe29a3
        , 0xbcc93cedfdb0d388, 0x4db312076ef0ad2b, 0x1f2cd56373654ad9, 0x4c6446970034d15f, 0x34d2cdbfd5d7130c, 0x6198950d03db2ae5, 0x736094b72faf1b1a, 0x1f6ca46a9f2588f7, 0xcba0b03d6259772a, 0x24e5a23d8d6be3a8, 0x7090e340c94f6d6f, 0x287ba27ee54e8466
        , 0x87320c8822d607f0, 0x44fd5802509df171, 0xf35c09860bf6ba4a, 0x6cf53130ef77cc0a, 0xaa81167a00b48ce4, 0x649f4c775b0d8b48, 0x59a25683ee98d33d, 0x651479007d1061a6, 0x155487411f6e16da, 0x411d036475404bf2, 0xc231f1344162458a, 0x4f36b7633f7dd368
        , 0xa98ddc0a4e7a89a4, 0x55d8a5da6eacd542, 0x5c3fb48b1001ed45, 0x5c7785ccafa702b9, 0xa64369fd216afb79, 0x1f405ef10e940669, 0x755f4831bc327b6f, 0x2bc1b67d71f1882d, 0x8eab15cfed7777d0, 0x517370d580d99326, 0x0811b75701c9db39, 0x234d84cb52f7b621
        , 0x970c4fbddddae49c, 0x3ba8d842475e41e1, 0xb0720f6ad75e7008, 0x275cd5c5184bf345, 0x5eb9833888d3796a, 0x1b3a42dfde11c2f3, 0x946548fe092b5f4d, 0x119917b50f263cc9, 0x622de955a20a3f82, 0x6a552ea3a60c7ff4, 0xc79230138150372a, 0x18083b9518de76a7
        , 0x55fb74dd7d3b5455, 0x523eea9a70ff8334, 0x5994a7335e356271, 0x3bb011f60430f1d2, 0x1ec434cba1d6ea7c, 0x69b632960feb5780, 0x46c50417541ebf07, 0x01470bfbf9d23830, 0xe9551f4c049bc5cc, 0x1c124638f35ee8ed, 0x09ca3a9141e83a38, 0x44daaf3e7411127b
        , 0x0e54717b6c2fcd10, 0x518ab46b26d5914b, 0x528ac6c82341e833, 0x2247fa99d41f4672, 0xabe30c65c0f327a2, 0x3ac74e012b77e1b4, 0x35defd694c0e86b3, 0x7c382e10bfe60e4e, 0xf37e382996b8461c, 0x4d47481c53631e1a, 0xac8f167884f7b7b1, 0x5ae1bb6ab1a4c643
        , 0x63eb02590829df80, 0x623126862a793fa1, 0x6e1e242f1ce09807, 0x7bf96130aaecfd2b, 0xedc5e9ea10bff70a, 0x66b548233b94d26e, 0x70c70ee4594d30ab, 0x79b0006c8811353e, 0x4352792c91710c1f, 0x0c7bf15181a9f539, 0xfc995ee769e3779c, 0x44871c6cb9dcedcd
        , 0x0d180bbf2c9a046b, 0x5445c598c45d0cd9, 0xdefb32386875fb94, 0x5b0d235355660f35, 0xbe1dea825b3a7973, 0x10658ec4e1bbe147, 0x48af5e87fad77504, 0x55f5d3c94a7dd694, 0xa9a3e7062cad6ba2, 0x36c0a7e3f9e0ea31, 0xc4bd65217010aebc, 0x1d031dfc8b9fb598
        , 0xe3621c104113889e, 0x774b77ee1e6a6477, 0x124c5b8a07785fd7, 0x5a6c0df18188cada, 0xf4adcd545e72d7be, 0x38100fffb66ba966, 0x2100cbe35fe4a4d0, 0x4489be2df052c175, 0xa03a22403b26899f, 0x5ae4a0a0fec13928, 0x89dfbfb802795eaa, 0x34917e9c4ecf2532
        , 0x64b93674c60cbbb3, 0x25c098506334c71d, 0x8a723f66f1ee34e1, 0x3a960adf48f141e4, 0x659f386695e440bb, 0x577a0fbf6e8095e6, 0x8ef419b0f4b25496, 0x044176a30b9e465b, 0x7a98705df2013e6f, 0x77d0b2483aa95ce7, 0x309e917b978effd7, 0x08f1e55bfe942c7f
        , 0xfc241629b8d613c8, 0x140f2e35cd68949f, 0x38899f6a3ee4f9fa, 0x7abc8ecdd300f3b5, 0xd3dad23505d23eaf, 0x75e73f09376b2c7c, 0x5644a663b60ec5c4, 0x511ade8afe1eaec9, 0xbb005fe4e1abca89, 0x2838de73b0ca1f6c, 0x800a6658b80d28c8, 0x48aaba61c91641ec
        , 0x222759cab704d4e2, 0x106dd3c0ce85beca, 0xa1ce1ce341f69d03, 0x1651b210e8e4ee10, 0x47329a5e7133e136, 0x58c02f47dc9367b9, 0x09dcba56947b02af, 0x435c251178125b48, 0xd56979a3f0cd9315, 0x2f02b0a6422afddb, 0x23920f500731f32d, 0x0ab833238232cb5d
        , 0xa7b3d1bfb0bb60db, 0x2342c2a03c6eaec2, 0xac5e6e5a14d5282e, 0x5b9a421ddc42a24b, 0x018506414543e056, 0x6d7c377c084954e6, 0x4f8bf71ed3db1ced, 0x5150dbc15ab10979, 0x00b50a1b373a7fbf, 0x140be5c3d3244705, 0x5005bfe96e5b7911, 0x77cea555bb133f3e
        , 0x2ab1e1a9d7a973c6, 0x3897ac98314968d3, 0x9e0f74764b23c9c3, 0x2e5ecbbae41997cd, 0x43e2ea5648f12433, 0x3a515a0e4808e69c, 0x17d36c03c36bb343, 0x44cebd053481ce43, 0x89008656c21b0d76, 0x2f8513fcb9009be6, 0x2e223f90208a0e83, 0x3828c2d4efd36a73
        , 0xbf17d64f89a8527d, 0x59ebb42b9656151d, 0x7d7bc7245c7dc5ef, 0x191b682a0cb695ec, 0x8931172fad9f9add, 0x239b6cbbab2ebdcf, 0x76932f9ca7002dd1, 0x0c140548f858d8b5, 0x6c7adfddcf741ea5, 0x3b39c4b9e2e1a567, 0xc5135a25f87436fe, 0x690d8fecb7dd0ae0
        , 0xd782a618ecda10c2, 0x4f2a84b3134cf832, 0x35a81f71bbc955a4, 0x457f88ed64ae6398, 0xc27eb71c31479985, 0x4ae91808569aab32, 0xa5f2e9785a75eb11, 0x619cb199b837ed36, 0x0e7e5912b9484e40, 0x3b5831e87fdbcaf0, 0x49a2779c2d2b039d, 0x3d4b81e07f49061a
        , 0xaa119b0fa222b55c, 0x265c1b11b42fd4e2, 0x6b4d28e519dd7637, 0x3d2da7900de5a4b2, 0x99b06586b5f21d63, 0x4ce62bd9e6a1ee18, 0xb671e753932f8c92, 0x390b7821d0987834, 0x1adf7c73c3f1fc2f, 0x78c636a8514a7af9, 0xaee3b35fe11e7533, 0x7fbd199278f6ffd7
        , 0x41aabbf4363d77de, 0x1b27fdf18b96bf6a, 0xda264a1dff9a981c, 0x36efc08530c0bf9a, 0x5bd8862a5d830854, 0x23d7c905e656e6cb, 0x4523324c5b64fdcf, 0x36627f376238665f, 0x564f53925c6d5ea4, 0x17c7cc86a1913022, 0xf90db52a543b009b, 0x15192dc91f8b994b
        , 0x80bfa3c1a79ec6e2, 0x48fca8ea99772ecc, 0xfee6a3b98c0f1824, 0x46a8c75601b81e22, 0x2cb3c402a8895fcc, 0x1d1dff9c04305ce2, 0xc1aefe78e85971d7, 0x79c6a083ab5a80b2, 0x379c7bca5dbf2518, 0x2419358989b3ca02, 0xc9c42c9cfa5f470e, 0x4481c2ce91b14459
        , 0x6b04dea1ea26deca, 0x26ee3ceee0d0a101, 0xe36cc6bcd8fa4f26, 0x4d14709719764fbd, 0xe0572a706f1fef52, 0x0f75fb69a23f2ec1, 0x32ae4b04a864cf3b, 0x0b6373a91b944773, 0x1a8f2bc20bd088af, 0x586b0d5ace401747, 0xa0e6b094a3c51433, 0x1752a123c268c1c7
        , 0x643c2a93b5770ea1, 0x536cb9d1b71eeb43, 0x6bfb0525d0cc6b3f, 0x1f4dcfeec3adefc3, 0x28a0169dd0bf57f0, 0x1336c9aa20a35449, 0xbbcda068703ad7a1, 0x5e33478283c1e03d, 0xf1997733d18fdaf2, 0x789af507a17bb867, 0x79970c14d5695613, 0x79452342e845256f
        , 0x6c12f9367a26a018, 0x11beda1c8f9cdfbe, 0x720e6ddf24b30929, 0x7706e91e3e544755, 0x4460381d3a6c9059, 0x7e01916c3678c424, 0x6024355a61d2bb07, 0x68bae01d79c869e2, 0xf21cbcff285df659, 0x02f7ee6aeb57c933, 0xce0f078c17266467, 0x039b4fdb5170a103
        , 0xd5de0fec61a4ae1b, 0x33d37a152a778695, 0xea64e40e6a10ded9, 0x1f1d394373bdb213, 0xf63598b6ef59fd14, 0x57922adc3ae52283, 0xe39a90e18b76f4a1, 0x27f3dbebd98a9dae, 0x18179dd9c03804b3, 0x511d72c1912e2d73, 0x88e1f6d24b2f3225, 0x56009999cdc2997f
        , 0xda6df977b7d82fe4, 0x76f746bba63da226, 0x0b5facfc3bf13bd7, 0x4a31eb04f66f0e18, 0x8ace73d5e7cfe28f, 0x19aa731bc30c20b1, 0xa91979fe73400317, 0x6795ce71a09c7c9f, 0x93d55501933700ba, 0x3850eaf08b1fd14d, 0x450c5abc89edca71, 0x1be5db848bdfa5ef
        , 0x77667d3f4fcf082b, 0x673b6e6c4824bc45, 0x6f22c12a5fe0ed6d, 0x006ee6722b5dfed1, 0xb47a13c1468d0c62, 0x40564879a378e6e4, 0x0bc6b553a9d3ab58, 0x21761c79e44dfcfd, 0x66f36ed3eb1050fb, 0x2e67df1312dd01d3, 0x48744c4a68dbf2ad, 0x7844962b6d6e039c
        , 0xe07b5675d378b65f, 0x336262aa3d2c1df0, 0x320a5667d78c2e2b, 0x4f668dd96dda5e2a, 0xe21556795c7b8470, 0x3061905b2ef82bb1, 0xaee53211472206b6, 0x1f87377fee0d7a39, 0xdac58c52a3b1a0c7, 0x6e3c4ce04f0d7ffd, 0xfdffec45d4a3990f, 0x4b5340f79e2ae2c2
        , 0x0537c8b7b3d1f332, 0x55292744ae35ee1a, 0x42336d0e6d057f1e, 0x5ac40e9e645cb3d7, 0x848f7b7f845e46c7, 0x74bda86736eff150, 0x891acf622baf4f35, 0x14bcef9cf39667bb, 0x9aa1354d9731b9b3, 0x27e855a19295e59f, 0x1a829a8e10662ed0, 0x3bbc43f9ec4437a7
        , 0x8bfa8b1cb1de5341, 0x3432778068d35549, 0xe3d807da41f25a48, 0x1bb6ee1ce2efe552, 0x08d9bded0bd3affc, 0x290f1c5299a917a8, 0xda8dfd79562f8939, 0x1bf7aae68686211f, 0x2ab6daf9bc860765, 0x7bef6e2f0eb58a0b, 0x8746faab7c439b94, 0x017ea87750bb8bda
        , 0xf8dfeb22239c9a7c, 0x35cec0d2887b3a13, 0x68aa94ac601f1606, 0x7470553f8ba61767, 0x37894f91c9eac410, 0x55b22aeb8337f732, 0x53f8d90f29a2fe94, 0x0aec068aec69023a, 0x40506162ad6182ee, 0x6a327ff1ac1e5475, 0x968d7095492df3c8, 0x3f93f46195f67521
        , 0x4983bca28970d546, 0x2716b931296b53c2, 0xf42b013266b6f8b3, 0x76f29b084b6a369f, 0x8e28749222216249, 0x4f2fa1d3a6c1acfd, 0x0ee66697eab8f954, 0x37c33e28fec0cce5, 0x7d0419e2bafd1dd1, 0x01f04d4299b94daa, 0x5ec06abbc1e5c7e6, 0x3a24c66060ed72a9
        , 0x0db764e15f960f26, 0x1d5973d5d59f9c3a, 0xf3dc2608dc6d9149, 0x1d80e0461b72f518, 0x2264dccd49c8b09c, 0x1f03e7a246334d5e, 0x2d6e38871b1fc2ad, 0x418588ae4f284bd3, 0x3efb071bafe1afa2, 0x0799ba0c80bdd8dc, 0xa6b273222dcc4a76, 0x13859f08ac8a4b23
        , 0x0194acc2663c5acb, 0x459fa55bd0bbedf6, 0x1b055550f06f8cc1, 0x09e5fad46599ea75, 0x6b3916ef772958a3, 0x4aaaa5c18093a431, 0x8e1503e36610f594, 0x620ef55048a263b9, 0x5a28963c8cb8ecbc, 0x6aee46b1b740c15a, 0x67e39606f59cfea9, 0x13a579e3777ca8b1
        , 0x45ad92f61cbb8de3, 0x53068a1a42460eab, 0x9b163546de379578, 0x07bf38a7cecd4860, 0xf84c77031d282de1, 0x402aed6399f78ffc, 0xfb83dd20295f6d45, 0x3702e257340d2ecd, 0xb8db2d8b979b97c8, 0x617526d2a50b0c51, 0xd86f6278313017db, 0x2f35eedec55f9d92
        , 0xeecb69493517973b, 0x7a111a74e0baf09a, 0xb82c6da8ec39f63d, 0x4217076312833746, 0x5d36d11f3dda88d9, 0x7baebcb360f2a887, 0x9829b62d093d6cbb, 0x10f17a2f6edf28fd, 0xfe3efa4353f40626, 0x731ca3065c118e34, 0x6185678827960895, 0x07f906a4f4c6355c
        , 0x361d9cd10e657142, 0x2b5f5d452dd861ce, 0xa3e01df05d04b69a, 0x533723bc4cfcc0db, 0x820384afa1bbccb5, 0x4e67e941595d8dfd, 0x0f8da50839e13646, 0x6887a0573a596968, 0xe93dd1df5ace7343, 0x0d4076f28ecf96c8, 0x0ba2f854988074c1, 0x5eb2a314a41a40b6
        , 0x49ff6d27a676b27e, 0x15f7ca40acd5114e, 0xc171f9a750d7da95, 0x3bedbe891f79eb5c, 0x5b643bceb83f74ff, 0x088b1af3aa331a4c, 0xde294c7e0a60c4a9, 0x0a0770fc8120b151, 0xf09b757a0c7c1937, 0x34b797c03efd9c88, 0x051e3edb2c28cc49, 0x66db34ec5ac5122c
        , 0x95fde0d3d3dc8cbf, 0x797897c8121818cf, 0x1fd46d197710f89d, 0x533a505803f809c5, 0xb60f1c090c9fd211, 0x4a7c3479af5c9d82, 0x4bfc3ffa4c8cf5a5, 0x6949f4a61306821f, 0xd814c949c67abcdc, 0x419a5e33166863c4, 0x9de646f6bd0895e0, 0x497cc1449a54545a
        , 0x69eb31247fe126f2, 0x323c83233967f477, 0x52e0db4d3d78127d, 0x42a0e188e7b9380c, 0x3a6b011c46e34e7e, 0x79f4168aa9a0b4aa, 0x94270a25d708fa4d, 0x2bb28618cbc9cdc8, 0x741e46bb04606819, 0x02790c52fb2ce982, 0x6dbb92d0c6d0af10, 0x32aa96ae061e9412
        , 0x1376700c90d98eaa, 0x4d1dfe650c0a7136, 0xb397f8eef89aff20, 0x4836ac4a041bae37, 0xf37c1076a80a02b8, 0x0d063fa2467b3a37, 0x498f2617b56b7e7b, 0x65ef1194db859a5d, 0xd1fe25d5d28ffcb6, 0x228ee6f49459c083, 0x6b7e82b3b009b15b, 0x713b185ef1fccbfc
        , 0x552468f1ff60c298, 0x2b7ba65d02519614, 0x8a86ad90ff0816c2, 0x7bf9249284bd02e5, 0x3008c56e474c2d10, 0x171473b77f804540, 0x15fb79d07bdea766, 0x66ac67c7b9b0951f, 0x34bca15bb6d2f652, 0x13c63dd2687d617b, 0xc515ae237715c19c, 0x0e543c6765fbfef2
        , 0x668c80faf156fb5e, 0x1e2e9e3b3d9962b8, 0x89ebaa264394e113, 0x322add21cf1659cf, 0xf9e6e26733619f8e, 0x723bfc8b792147f0, 0x79aef2837d7e092f, 0x1aa61c59290b5011, 0x9955ae576a499cd3, 0x2c3d6e6a5a1ce0da, 0xb864cfa199a8676b, 0x4961a21f1080285f
        , 0x828e184adf9d997b, 0x0c84bda97e7ce725, 0xe6974677094cfcc5, 0x4ec8cd773946105b, 0xa48681bcc95fb5c6, 0x6ade87f8f7a5f269, 0x9b97628fdd39c03d, 0x3bde0ee1f19f1842, 0x4ef8c8fb117c0ca1, 0x769bf8f8d07de9bf, 0xc8f5f435b78a57e5, 0x79987aa861bbcf9c
        , 0x7f6c557204b02022, 0x119bd819111c69d1, 0xf0c61ef00b3eb70b, 0x4317f0511bfb7b39, 0x36a2b944e84d608e, 0x1c1a3862da3369cb, 0x37dbf471085f1775, 0x3835751e107419ad, 0x04ab0c84bb07a3fe, 0x63758bfbc7df13a0, 0x15ffd20cb554f23e, 0x1ff11c442b1515b7
        , 0x171377f1bf937186, 0x615efe82b83538f8, 0x321e7cfae352a761, 0x7af02427d7241502, 0x86546e47f2cc559f, 0x65a1d8a017659d75, 0xc95d8aa5b8bfdac9, 0x01e887cb68990623, 0xf1f8ee8c466bcc3d, 0x40ce5e4f2ba3908f, 0xd2b81a3480c16b35, 0x51625d3eabf708cd
        , 0x44d770a210105739, 0x7f1de74a022958a0, 0xfbe4c91bd1e8f732, 0x204fbacb13586460, 0x97d79097d62e3cf8, 0x541ad5591934b114, 0xfdfb47919c141909, 0x354926e5244fdecf, 0x6291b0a0e2e994b0, 0x2b9a9a69d3a6c3d1, 0x8189be54302371e7, 0x3645c65df1a881cd
        , 0xdf0460f445e3877b, 0x7ea384dc52d0d26e, 0x0c2e5f768d46b6b0, 0x1f6e62daa7c5d4e6, 0xf8b026b33b2343ee, 0x2b7183c8767d372c, 0xbd45d1b6b6731517, 0x4ddb3d287c470d60, 0x1031dba40263ece2, 0x4e737fa0d659045f, 0x8cbc98d07d09b455, 0x34a35128a2bcb7f5 };

#if __aarch64__
static inline unsigned char _subborrow_u64(unsigned char b_in, unsigned long long src1, unsigned long long src2, unsigned long long *diff_out)
{
    *diff_out = src1 - (src2 + (b_in !=0 ? 1 : 0));
    if (src1 < src2+(b_in !=0 ? 1 : 0)) return 1;
    return 0;
}
static inline unsigned char _addcarry_u64(unsigned char b_in, unsigned long long src1, unsigned long long src2, unsigned long long *sum_out)
{
    *sum_out = src1 + (src2 + (b_in !=0 ? 1 : 0));

    if (UINT64_MAX-src1 < src2+(b_in !=0 ? 1 : 0)) return 1;
    return 0;
}
#endif

static void mod1271(felm_t a)
{ // Modular correction, a = a mod (2^127-1)
    _subborrow_u64(_subborrow_u64(0, a[0], 0xFFFFFFFFFFFFFFFF, &a[0]), a[1], 0x7FFFFFFFFFFFFFFF, &a[1]);
    unsigned long long mask = 0 - (a[1] >> 63);
    _addcarry_u64(_addcarry_u64(0, a[0], mask, &a[0]), a[1], 0x7FFFFFFFFFFFFFFF & mask, &a[1]);
}

static void fpadd1271(felm_t a, felm_t b, felm_t c)
{ // Field addition, c = a+b mod (2^127-1)
    _addcarry_u64(_addcarry_u64(0, a[0], b[0], &c[0]), a[1], b[1], &c[1]);
    _addcarry_u64(_addcarry_u64(0, c[0], c[1] >> 63, &c[0]), c[1] & 0x7FFFFFFFFFFFFFFF, 0, &c[1]);
}

static void fpsub1271(felm_t a, felm_t b, felm_t c)
{ // Field subtraction, c = a-b mod (2^127-1)
    _subborrow_u64(_subborrow_u64(0, a[0], b[0], &c[0]), a[1], b[1], &c[1]);
    _subborrow_u64(_subborrow_u64(0, c[0], c[1] >> 63, &c[0]), c[1] & 0x7FFFFFFFFFFFFFFF, 0, &c[1]);
}

static void fpneg1271(felm_t a)
{ // Field negation, a = -a mod (2^127-1)
    a[0] = ~a[0];
    a[1] = 0x7FFFFFFFFFFFFFFF - a[1];
}
#ifndef _MSC_VER
static uint64_t _umul128(uint64_t a, uint64_t b, long long unsigned int *hi)
{
    union { unsigned __int128 v; uint64_t sv[2]; } var;
    var.v = a;
    var.v *= b;
    if (hi) *hi = var.sv[1];
    return var.sv[0];
}


#ifndef _MSC_VER
static uint64_t __shiftleft128 (uint64_t  LowPart, uint64_t HighPart, uint8_t Shift)
{
#if __aarch64__
    __uint128_t a = (((__uint128_t)(HighPart)) << 64) | LowPart;
    a = a << Shift;
    return (a>>64) & 0xFFFFFFFFFFFFFFFFULL;
#else
    uint64_t ret;
    __asm__ ("shld {%[Shift],%[LowPart],%[HighPart]|%[HighPart], %[LowPart], %[Shift]}"
            : [ret] "=r" (ret)
    : [LowPart] "r" (LowPart), [HighPart] "0" (HighPart), [Shift] "Jc" (Shift)
    : "cc");
    return ret;
#endif
}

static uint64_t __shiftright128 (uint64_t  LowPart, uint64_t HighPart, uint8_t Shift)
{
#if __aarch64__
    __uint128_t a = (((__uint128_t)(HighPart)) << 64) | LowPart;
    a = a >> Shift;
    return a & 0xFFFFFFFFFFFFFFFFULL;
#else
    uint64_t ret;
    __asm__ ("shrd {%[Shift],%[HighPart],%[LowPart]|%[LowPart], %[HighPart], %[Shift]}"
            : [ret] "=r" (ret)
    : [LowPart] "0" (LowPart), [HighPart] "r" (HighPart), [Shift] "Jc" (Shift)
    : "cc");

    return ret;
#endif
}
#endif
#endif

static void fpmul1271(felm_t a, felm_t b, felm_t c)
{ // Field multiplication, c = a*b mod (2^127-1)
    unsigned long long tt1[2], tt2[2], tt3[2];

    tt1[0] = _umul128(a[0], b[0], &tt3[0]);
    tt2[0] = _umul128(a[0], b[1], &tt2[1]);
    _addcarry_u64(_addcarry_u64(0, tt2[0], tt3[0], &tt2[0]), tt2[1], 0, &tt2[1]);
    tt3[0] = _umul128(a[1], b[0], &tt3[1]);
    _addcarry_u64(_addcarry_u64(0, tt2[0], tt3[0], &tt2[0]), tt2[1], tt3[1], &tt2[1]);
    tt3[0] = _umul128(a[1], b[1], &tt3[1]);
    tt3[1] = __shiftleft128(tt3[0], tt3[1], 1);
    _addcarry_u64(_addcarry_u64(0, __shiftright128(tt2[0], tt2[1], 63), tt3[0] << 1, &tt3[0]), tt2[1] >> 63, tt3[1], &tt3[1]);
    _addcarry_u64(_addcarry_u64(0, tt1[0], tt3[0], &tt1[0]), tt2[0] & 0x7FFFFFFFFFFFFFFF, tt3[1], &tt1[1]);
    _addcarry_u64(_addcarry_u64(0, tt1[0], tt1[1] >> 63, &c[0]), tt1[1] & 0x7FFFFFFFFFFFFFFF, 0, &c[1]);
}

static void fpsqr1271(felm_t a, felm_t c)
{ // Field squaring, c = a^2 mod (2^127-1)
    unsigned long long tt1[2], tt2[2], tt3[2];

    tt1[0] = _umul128(a[0], a[0], &tt3[0]);
    tt2[0] = _umul128(a[0], a[1], &tt2[1]);
    _addcarry_u64(_addcarry_u64(0, tt2[0], tt3[0], &tt3[0]), tt2[1], 0, &tt3[1]);
    _addcarry_u64(_addcarry_u64(0, tt2[0], tt3[0], &tt2[0]), tt2[1], tt3[1], &tt2[1]);
    tt3[0] = _umul128(a[1], a[1], &tt3[1]);
    tt3[1] = __shiftleft128(tt3[0], tt3[1], 1);
    _addcarry_u64(_addcarry_u64(0, __shiftright128(tt2[0], tt2[1], 63), tt3[0] << 1, &tt3[0]), tt2[1] >> 63, tt3[1], &tt3[1]);
    _addcarry_u64(_addcarry_u64(0, tt1[0], tt3[0], &tt1[0]), tt2[0] & 0x7FFFFFFFFFFFFFFF, tt3[1], &tt1[1]);
    _addcarry_u64(_addcarry_u64(0, tt1[0], tt1[1] >> 63, &c[0]), tt1[1] & 0x7FFFFFFFFFFFFFFF, 0, &c[1]);
}

static void fpexp1251(felm_t a, felm_t af)
{ // Exponentiation over GF(p), af = a^(125-1)
    felm_t t1, t2, t3, t4, t5;

    fpsqr1271(a, t2);
    fpmul1271(a, t2, t2);
    fpsqr1271(t2, t3);
    fpsqr1271(t3, t3);
    fpmul1271(t2, t3, t3);
    fpsqr1271(t3, t4);
    fpsqr1271(t4, t4);
    fpsqr1271(t4, t4);
    fpsqr1271(t4, t4);
    fpmul1271(t3, t4, t4);
    fpsqr1271(t4, t5);
    for (unsigned int i = 0; i < 7; i++) fpsqr1271(t5, t5);
    fpmul1271(t4, t5, t5);
    fpsqr1271(t5, t2);
    for (unsigned int i = 0; i < 15; i++) fpsqr1271(t2, t2);
    fpmul1271(t5, t2, t2);
    fpsqr1271(t2, t1);
    for (unsigned int i = 0; i < 31; i++) fpsqr1271(t1, t1);
    fpmul1271(t2, t1, t1);
    for (unsigned int i = 0; i < 32; i++) fpsqr1271(t1, t1);
    fpmul1271(t1, t2, t1);
    for (unsigned int i = 0; i < 16; i++) fpsqr1271(t1, t1);
    fpmul1271(t5, t1, t1);
    for (unsigned int i = 0; i < 8; i++) fpsqr1271(t1, t1);
    fpmul1271(t4, t1, t1);
    for (unsigned int i = 0; i < 4; i++) fpsqr1271(t1, t1);
    fpmul1271(t3, t1, t1);
    fpsqr1271(t1, t1);
    fpmul1271(a, t1, af);
}

static void fp2div1271(f2elm_t a)
{ // GF(p^2) division by two c = a/2 mod p
    unsigned long long mask, temp[2];

    mask = (0 - (1 & a[0][0]));
    _addcarry_u64(_addcarry_u64(0, a[0][0], mask, &temp[0]), a[0][1], (mask >> 1), &temp[1]);
    a[0][0] = __shiftright128(temp[0], temp[1], 1);
    a[0][1] = (temp[1] >> 1);

    mask = (0 - (1 & a[1][0]));
    _addcarry_u64(_addcarry_u64(0, a[1][0], mask, &temp[0]), a[1][1], (mask >> 1), &temp[1]);
    a[1][0] = __shiftright128(temp[0], temp[1], 1);
    a[1][1] = (temp[1] >> 1);
}

static void fp2neg1271(f2elm_t a)
{ // GF(p^2) negation, a = -a in GF((2^127-1)^2)
    fpneg1271(a[0]);
    fpneg1271(a[1]);
}

static void fp2sqr1271(f2elm_t a, f2elm_t c)
{ // GF(p^2) squaring, c = a^2 in GF((2^127-1)^2)
    felm_t t1, t2, t3;

    fpadd1271(a[0], a[1], t1);           // t1 = a0+a1
    fpsub1271(a[0], a[1], t2);           // t2 = a0-a1
    fpmul1271(a[0], a[1], t3);           // t3 = a0*a1
    fpmul1271(t1, t2, c[0]);             // c0 = (a0+a1)(a0-a1)
    fpadd1271(t3, t3, c[1]);             // c1 = 2a0*a1
}

static void fp2mul1271(f2elm_t a, f2elm_t b, f2elm_t c)
{ // GF(p^2) multiplication, c = a*b in GF((2^127-1)^2)
    felm_t t1, t2, t3, t4;

    fpmul1271(a[0], b[0], t1);          // t1 = a0*b0
    fpmul1271(a[1], b[1], t2);          // t2 = a1*b1
    fpadd1271(a[0], a[1], t3);          // t3 = a0+a1
    fpadd1271(b[0], b[1], t4);          // t4 = b0+b1
    fpsub1271(t1, t2, c[0]);            // c[0] = a0*b0 - a1*b1
    fpmul1271(t3, t4, t3);              // t3 = (a0+a1)*(b0+b1)
    fpsub1271(t3, t1, t3);              // t3 = (a0+a1)*(b0+b1) - a0*b0
    fpsub1271(t3, t2, c[1]);            // c[1] = (a0+a1)*(b0+b1) - a0*b0 - a1*b1
}

static void fp2add1271(f2elm_t a, f2elm_t b, f2elm_t c)
{ // GF(p^2) addition, c = a+b in GF((2^127-1)^2)
    fpadd1271(a[0], b[0], c[0]);
    fpadd1271(a[1], b[1], c[1]);
}

static void fp2sub1271(f2elm_t a, f2elm_t b, f2elm_t c)
{ // GF(p^2) subtraction, c = a-b in GF((2^127-1)^2)
    fpsub1271(a[0], b[0], c[0]);
    fpsub1271(a[1], b[1], c[1]);
}

static void fp2addsub1271(f2elm_t a, f2elm_t b, f2elm_t c)
{ // GF(p^2) addition followed by subtraction, c = 2a-b in GF((2^127-1)^2)

    fp2add1271(a, a, a);
    fp2sub1271(a, b, c);
}

static inline void copy32(unsigned char* dst, const unsigned char* src)
{
    memcpy(dst, src, 32);
}

static void table_lookup_fixed_base(point_precomp_t P, unsigned int digit, unsigned int sign)
{ // Table lookup to extract a point represented as (x+y,y-x,2t) corresponding to extended twisted Edwards coordinates (X:Y:Z:T) with Z=1
    if (sign)
    {
        copy32((uint8_t*)P->xy, (uint8_t*)((point_precomp_t*)FIXED_BASE_TABLE)[digit]->yx);
        copy32((uint8_t*)P->yx, (uint8_t*)((point_precomp_t*)FIXED_BASE_TABLE)[digit]->xy);
        P->t2[0][0] = ~(((point_precomp_t*)FIXED_BASE_TABLE)[digit])->t2[0][0];
        P->t2[0][1] = 0x7FFFFFFFFFFFFFFF - (((point_precomp_t*)FIXED_BASE_TABLE)[digit])->t2[0][1];
        P->t2[1][0] = ~(((point_precomp_t*)FIXED_BASE_TABLE)[digit])->t2[1][0];
        P->t2[1][1] = 0x7FFFFFFFFFFFFFFF - (((point_precomp_t*)FIXED_BASE_TABLE)[digit])->t2[1][1];
    }
    else
    {
        copy32((uint8_t*)P->xy, (uint8_t*)((point_precomp_t*)FIXED_BASE_TABLE)[digit]->xy);
        copy32((uint8_t*)P->yx, (uint8_t*)((point_precomp_t*)FIXED_BASE_TABLE)[digit]->yx);
        copy32((uint8_t*)P->t2, (uint8_t*)((point_precomp_t*)FIXED_BASE_TABLE)[digit]->t2);
    }
}

static void multiply(const unsigned long long* a, const unsigned long long* b, unsigned long long* c)
{
    unsigned long long u, v, uv;

    c[0] = _umul128(a[0], b[0], &u);
    u = _addcarry_u64(0, _umul128(a[0], b[1], &uv), u, &c[1]) + uv;
    u = _addcarry_u64(0, _umul128(a[0], b[2], &uv), u, &c[2]) + uv;
    c[4] = _addcarry_u64(0, _umul128(a[0], b[3], &uv), u, &c[3]) + uv;

    u = _addcarry_u64(0, c[1], _umul128(a[1], b[0], &uv), &c[1]) + uv;
    u = _addcarry_u64(0, _umul128(a[1], b[1], &uv), u, &v) + uv;
    u = _addcarry_u64(_addcarry_u64(0, c[2], v, &c[2]), _umul128(a[1], b[2], &uv), u, &v) + uv;
    c[5] = _addcarry_u64(_addcarry_u64(0, c[3], v, &c[3]), _umul128(a[1], b[3], &uv), u, &v) + uv + _addcarry_u64(0, c[4], v, &c[4]);

    u = _addcarry_u64(0, c[2], _umul128(a[2], b[0], &uv), &c[2]) + uv;
    u = _addcarry_u64(0, _umul128(a[2], b[1], &uv), u, &v) + uv;
    u = _addcarry_u64(_addcarry_u64(0, c[3], v, &c[3]), _umul128(a[2], b[2], &uv), u, &v) + uv;
    c[6] = _addcarry_u64(_addcarry_u64(0, c[4], v, &c[4]), _umul128(a[2], b[3], &uv), u, &v) + uv + _addcarry_u64(0, c[5], v, &c[5]);

    u = _addcarry_u64(0, c[3], _umul128(a[3], b[0], &uv), &c[3]) + uv;
    u = _addcarry_u64(0, _umul128(a[3], b[1], &uv), u, &v) + uv;
    u = _addcarry_u64(_addcarry_u64(0, c[4], v, &c[4]), _umul128(a[3], b[2], &uv), u, &v) + uv;
    c[7] = _addcarry_u64(_addcarry_u64(0, c[5], v, &c[5]), _umul128(a[3], b[3], &uv), u, &v) + uv + _addcarry_u64(0, c[6], v, &c[6]);
}

static void Montgomery_multiply_mod_order(const unsigned long long* ma, const unsigned long long* mb, unsigned long long* mc)
{ // 256-bit Montgomery multiplication modulo the curve order, mc = ma*mb*r' mod order, where ma,mb,mc in [0, order-1]
    // ma, mb and mc are assumed to be in Montgomery representation
    // The Montgomery constant r' = -r^(-1) mod 2^(log_2(r)) is the global value "Montgomery_rprime", where r is the order
    unsigned long long P[8];
    unsigned long long Q[4];
    unsigned long long temp[8];

    if (mb[0] == 1 && !mb[1] && !mb[2] && !mb[3])
    {
        memcpy(P, ma, 32);
        memset( ((uint8_t*)P) + 32, 0, 32);
    }
    else
    {
        multiply(ma, mb, P); // P = ma * mb
    }

    unsigned long long u, v, uv;
    Q[0] = _umul128(P[0], MONTGOMERY_SMALL_R_PRIME_0, &u);
    u = _addcarry_u64(0, _umul128(P[0], MONTGOMERY_SMALL_R_PRIME_1, &uv), u, &Q[1]) + uv;
    u = _addcarry_u64(0, _umul128(P[0], MONTGOMERY_SMALL_R_PRIME_2, &uv), u, &Q[2]) + uv;
    _addcarry_u64(0, P[0] * MONTGOMERY_SMALL_R_PRIME_3, u, &Q[3]);
    u = _addcarry_u64(0, Q[1], _umul128(P[1], MONTGOMERY_SMALL_R_PRIME_0, &uv), &Q[1]) + uv;
    u = _addcarry_u64(0, _umul128(P[1], MONTGOMERY_SMALL_R_PRIME_1, &uv), u, &v) + uv;
    _addcarry_u64(_addcarry_u64(0, Q[2], v, &Q[2]), P[1] * MONTGOMERY_SMALL_R_PRIME_2, u, &v);
    _addcarry_u64(0, Q[3], v, &Q[3]);
    u = _addcarry_u64(0, Q[2], _umul128(P[2], MONTGOMERY_SMALL_R_PRIME_0, &uv), &Q[2]) + uv;
    _addcarry_u64(0, P[2] * MONTGOMERY_SMALL_R_PRIME_1, u, &v);
    _addcarry_u64(0, Q[3], v, &Q[3]);
    _addcarry_u64(0, Q[3], P[3] * MONTGOMERY_SMALL_R_PRIME_0, &Q[3]);

    multiply(Q, curve_order, temp); // temp = Q * r

    if (_addcarry_u64(_addcarry_u64(_addcarry_u64(_addcarry_u64(_addcarry_u64(_addcarry_u64(_addcarry_u64(_addcarry_u64(0, P[0], temp[0], &temp[0]), P[1], temp[1], &temp[1]), P[2], temp[2], &temp[2]), P[3], temp[3], &temp[3]), P[4], temp[4], &temp[4]), P[5], temp[5], &temp[5]), P[6], temp[6], &temp[6]), P[7], temp[7], &temp[7])
        - _subborrow_u64(_subborrow_u64(_subborrow_u64(_subborrow_u64(0, temp[4], CURVE_ORDER_0, &mc[0]), temp[5], CURVE_ORDER_1, &mc[1]), temp[6], CURVE_ORDER_2, &mc[2]), temp[7], CURVE_ORDER_3, &mc[3]))
    {
        _addcarry_u64(_addcarry_u64(_addcarry_u64(_addcarry_u64(0, mc[0], CURVE_ORDER_0, &mc[0]), mc[1], CURVE_ORDER_1, &mc[1]), mc[2], CURVE_ORDER_2, &mc[2]), mc[3], CURVE_ORDER_3, &mc[3]);
    }
}

static void eccnorm(point_extproj_t P, point_t Q)
{ // Normalize a projective point (X1:Y1:Z1), including full reduction

    // Z1 = Z1^-1
    f2elm_t t1;
    fpsqr1271(P->z[0], t1[0]);
    fpsqr1271(P->z[1], t1[1]);
    fpadd1271(t1[0], t1[1], t1[0]);
    fpexp1251(t1[0], t1[1]);
    fpsqr1271(t1[1], t1[1]);
    fpsqr1271(t1[1], t1[1]);
    fpmul1271(t1[0], t1[1], t1[0]);
    fpneg1271(P->z[1]);
    fpmul1271(P->z[0], t1[0], P->z[0]);
    fpmul1271(P->z[1], t1[0], P->z[1]);

    fp2mul1271(P->x, P->z, Q->x);          // X1 = X1/Z1
    fp2mul1271(P->y, P->z, Q->y);          // Y1 = Y1/Z1
    mod1271(Q->x[0]);
    mod1271(Q->x[1]);
    mod1271(Q->y[0]);
    mod1271(Q->y[1]);
}

static void R1_to_R2(point_extproj_t P, point_extproj_precomp_t Q)
{ // Conversion from representation (X,Y,Z,Ta,Tb) to (X+Y,Y-X,2Z,2dT), where T = Ta*Tb
    fp2add1271(P->ta, P->ta, Q->t2);                  // T = 2*Ta
    fp2add1271(P->x, P->y, Q->xy);                    // QX = X+Y
    fp2sub1271(P->y, P->x, Q->yx);                    // QY = Y-X
    fp2mul1271(Q->t2, P->tb, Q->t2);                  // T = 2*T
    fp2add1271(P->z, P->z, Q->z2);                    // QZ = 2*Z
    fp2mul1271(Q->t2, (felm_t*)&PARAMETER_d, Q->t2);  // QT = 2d*T
}

static void R1_to_R3(point_extproj_t P, point_extproj_precomp_t Q)
{ // Conversion from representation (X,Y,Z,Ta,Tb) to (X+Y,Y-X,Z,T), where T = Ta*Tb
    fp2add1271(P->x, P->y, Q->xy);         // XQ = (X1+Y1)
    fp2sub1271(P->y, P->x, Q->yx);         // YQ = (Y1-X1)
    fp2mul1271(P->ta, P->tb, Q->t2);       // TQ = T1
    copy32((uint8_t*)Q->z2, (uint8_t*)&P->z);
}

static void R2_to_R4(point_extproj_precomp_t P, point_extproj_t Q)
{ // Conversion from representation (X+Y,Y-X,2Z,2dT) to (2X,2Y,2Z,2dT)
    fp2sub1271(P->xy, P->yx, Q->x);        // XQ = 2*X1
    fp2add1271(P->xy, P->yx, Q->y);        // YQ = 2*Y1
    copy32((uint8_t*)Q->z, (uint8_t*)&P->z2);
}

static void eccdouble(point_extproj_t P)
{ // Point doubling 2P
    f2elm_t t1, t2;

    fp2sqr1271(P->x, t1);                  // t1 = X1^2
    fp2sqr1271(P->y, t2);                  // t2 = Y1^2
    fp2add1271(P->x, P->y, P->x);          // t3 = X1+Y1
    fp2add1271(t1, t2, P->tb);             // Tbfinal = X1^2+Y1^2
    fp2sub1271(t2, t1, t1);                // t1 = Y1^2-X1^2
    fp2sqr1271(P->x, P->ta);               // Ta = (X1+Y1)^2
    fp2sqr1271(P->z, t2);                  // t2 = Z1^2
    fp2sub1271(P->ta, P->tb, P->ta);       // Tafinal = 2X1*Y1 = (X1+Y1)^2-(X1^2+Y1^2)
    fp2addsub1271(t2, t1, t2);             // t2 = 2Z1^2-(Y1^2-X1^2)
    fp2mul1271(t1, P->tb, P->y);           // Yfinal = (X1^2+Y1^2)(Y1^2-X1^2)
    fp2mul1271(t2, P->ta, P->x);           // Xfinal = 2X1*Y1*[2Z1^2-(Y1^2-X1^2)]
    fp2mul1271(t1, t2, P->z);              // Zfinal = (Y1^2-X1^2)[2Z1^2-(Y1^2-X1^2)]
}

static void eccadd_core(point_extproj_precomp_t P, point_extproj_precomp_t Q, point_extproj_t R)
{ // Basic point addition R = P+Q or R = P+P
    f2elm_t t1, t2;

    fp2mul1271(P->t2, Q->t2, R->z);        // Z = 2dT1*T2
    fp2mul1271(P->z2, Q->z2, t1);          // t1 = 2Z1*Z2
    fp2mul1271(P->xy, Q->xy, R->x);        // X = (X1+Y1)(X2+Y2)
    fp2mul1271(P->yx, Q->yx, R->y);        // Y = (Y1-X1)(Y2-X2)
    fp2sub1271(t1, R->z, t2);              // t2 = theta
    fp2add1271(t1, R->z, t1);              // t1 = alpha
    fp2sub1271(R->x, R->y, R->tb);         // Tbfinal = beta
    fp2add1271(R->x, R->y, R->ta);         // Tafinal = omega
    fp2mul1271(R->tb, t2, R->x);           // Xfinal = beta*theta
    fp2mul1271(t1, t2, R->z);              // Zfinal = theta*alpha
    fp2mul1271(R->ta, t1, R->y);           // Yfinal = alpha*omega
}

static void eccadd(point_extproj_precomp_t Q, point_extproj_t P)
{ // Complete point addition P = P+Q or P = P+P
    point_extproj_precomp_t R;

    R1_to_R3(P, R);                        // R = (X1+Y1,Y1-Z1,Z1,T1)
    eccadd_core(Q, R, P);                  // P = (X2+Y2,Y2-X2,2Z2,2dT2) + (X1+Y1,Y1-Z1,Z1,T1)
}

static void point_setup(point_t P, point_extproj_t Q)
{ // Point conversion to representation (X,Y,Z,Ta,Tb)
    copy32((uint8_t*)Q->x, (uint8_t*)&P->x);
    copy32((uint8_t*)Q->y, (uint8_t*)&P->y);
    copy32((uint8_t*)Q->ta, (uint8_t*)&Q->x);
    copy32((uint8_t*)Q->tb, (uint8_t*)&Q->y);
    Q->z[0][0] = 1; Q->z[0][1] = 0; Q->z[1][0] = 0; Q->z[1][1] = 0; // Z1 = 1
}

static bool ecc_point_validate(point_extproj_t P)
{ // Point validation: check if point lies on the curve
    f2elm_t t1, t2, t3;

    fp2sqr1271(P->y, t1);
    fp2sqr1271(P->x, t2);
    fp2sub1271(t1, t2, t3);                                 // -x^2 + y^2
    fp2mul1271(t1, t2, t1);                                 // x^2*y^2
    fp2mul1271(t1, (felm_t*)&PARAMETER_d, t2);              // dx^2*y^2
    t1[0][0] = 1; t1[0][1] = 0; t1[1][0] = 0; t1[1][1] = 0; // t1 = 1
    fp2add1271(t2, t1, t2);                                 // 1 + dx^2*y^2
    fp2sub1271(t3, t2, t1);                                 // -x^2 + y^2 - 1 - dx^2*y^2

    return ((!(t1[0][0] | t1[0][1]) || !((t1[0][0] + 1) | (t1[0][1] + 1)))
            && (!(t1[1][0] | t1[1][1]) || !((t1[1][0] + 1) | (t1[1][1] + 1))));
}

static void eccmadd(point_precomp_t Q, point_extproj_t P)
{ // Mixed point addition P = P+Q or P = P+P
    f2elm_t t1, t2;

    fp2mul1271(P->ta, P->tb, P->ta);        // Ta = T1
    fp2add1271(P->z, P->z, t1);             // t1 = 2Z1
    fp2mul1271(P->ta, Q->t2, P->ta);        // Ta = 2dT1*t2
    fp2add1271(P->x, P->y, P->z);           // Z = (X1+Y1)
    fp2sub1271(P->y, P->x, P->tb);          // Tb = (Y1-X1)
    fp2sub1271(t1, P->ta, t2);              // t2 = theta
    fp2add1271(t1, P->ta, t1);              // t1 = alpha
    fp2mul1271(Q->xy, P->z, P->ta);         // Ta = (X1+Y1)(x2+y2)
    fp2mul1271(Q->yx, P->tb, P->x);         // X = (Y1-X1)(y2-x2)
    fp2mul1271(t1, t2, P->z);               // Zfinal = theta*alpha
    fp2sub1271(P->ta, P->x, P->tb);         // Tbfinal = beta
    fp2add1271(P->ta, P->x, P->ta);         // Tafinal = omega
    fp2mul1271(P->tb, t2, P->x);            // Xfinal = beta*theta
    fp2mul1271(P->ta, t1, P->y);            // Yfinal = alpha*omega
}

VOID_FUNC_DECL ecc_mul_fixed(unsigned long long* k, point_t Q)
{ // Fixed-base scalar multiplication Q = k*G, where G is the generator. FIXED_BASE_TABLE stores v*2^(w-1) = 80 multiples of G.
    unsigned int digits[250];
    unsigned long long scalar[4];

    Montgomery_multiply_mod_order(k, Montgomery_Rprime, scalar);
    Montgomery_multiply_mod_order(scalar, ONE, scalar);


    // Converting scalar to odd using the prime subgroup order
    // If (k is odd) then k_odd = k else k_odd = k + r
    if (!(scalar[0] & 1))
    {
        uint8_t carry = _addcarry_u64(0, scalar[0], CURVE_ORDER_0, &scalar[0]);
        carry = _addcarry_u64(carry, scalar[1], CURVE_ORDER_1, &scalar[1]);
        carry = _addcarry_u64(carry, scalar[2], CURVE_ORDER_2, &scalar[2]);
        _addcarry_u64(carry, scalar[3], CURVE_ORDER_3, &scalar[3]);
    }

    // Shift scalar to the right by 1
    scalar[0] = __shiftright128(scalar[0], scalar[1], 1);
    scalar[1] = __shiftright128(scalar[1], scalar[2], 1);
    scalar[2] = __shiftright128(scalar[2], scalar[3], 1);
    scalar[3] >>= 1;

    for (unsigned int i = 0; i < 49; i++)
    {
        digits[i] = (unsigned int)((scalar[0] & 1) - 1);  // Convention for the "sign" row: if scalar_(i+1) = 0 then digit_i = -1 (negative), else if scalar_(i+1) = 1 then digit_i = 0 (positive)

        // Shift scalar to the right by 1
        scalar[0] = __shiftright128(scalar[0], scalar[1], 1);
        scalar[1] = __shiftright128(scalar[1], scalar[2], 1);
        scalar[2] = __shiftright128(scalar[2], scalar[3], 1);
        scalar[3] >>= 1;
    }
    digits[49] = 0;
    for (unsigned int i = 50; i < 250; i++)
    {
        digits[i] = (unsigned int)(scalar[0] & 1); // digits_i = k mod 2. Sign is determined by the "sign" row

        // Shift scalar to the right by 1
        scalar[0] = __shiftright128(scalar[0], scalar[1], 1);
        scalar[1] = __shiftright128(scalar[1], scalar[2], 1);
        scalar[2] = __shiftright128(scalar[2], scalar[3], 1);
        scalar[3] >>= 1;

        const unsigned long long temp = (0 - digits[i - (i / 50) * 50]) & digits[i]; // if (digits_i=0 \/ 1) then temp = 0, else if (digits_i=-1) then temp = 1

        // floor(scalar/2) + temp
        scalar[0] += temp;
        unsigned long long carry = scalar[0] ? 0 : (temp & 1); // carry = (scalar[0] < temp);
        scalar[1] += carry;
        carry = scalar[1] ? 0 : (carry & 1); // carry = (scalar[j] < temp);
        scalar[2] += carry;
        scalar[3] += (scalar[2] ? 0 : (carry & 1)); // carry = (scalar[j] < temp);
    }

    point_extproj_t R;
    point_precomp_t S;

    table_lookup_fixed_base(S, 64 + (((((digits[249] << 1) + digits[199]) << 1) + digits[149]) << 1) + digits[99], 0);
    // Conversion from representation (x+y,y-x,2dt) to (X,Y,Z,Ta,Tb)
    fp2sub1271(S->xy, S->yx, R->x);                                 // 2*x1
    fp2add1271(S->xy, S->yx, R->y);                                 // 2*y1
    fp2div1271(R->x);                                               // XQ = x1
    fp2div1271(R->y);                                               // YQ = y1
    R->z[0][0] = 1; R->z[0][1] = 0; R->z[1][0] = 0; R->z[1][1] = 0; // ZQ = 1
    copy32((uint8_t*)R->ta, (uint8_t*)&R->x);
    copy32((uint8_t*)R->tb, (uint8_t*)&R->y);

    table_lookup_fixed_base(S, 48 + (((((digits[239] << 1) + digits[189]) << 1) + digits[139]) << 1) + digits[89], digits[39]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[229] << 1) + digits[179]) << 1) + digits[129]) << 1) + digits[79], digits[29]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[219] << 1) + digits[169]) << 1) + digits[119]) << 1) + digits[69], digits[19]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[209] << 1) + digits[159]) << 1) + digits[109]) << 1) + digits[59], digits[9]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[248] << 1) + digits[198]) << 1) + digits[148]) << 1) + digits[98], digits[48]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[238] << 1) + digits[188]) << 1) + digits[138]) << 1) + digits[88], digits[38]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[228] << 1) + digits[178]) << 1) + digits[128]) << 1) + digits[78], digits[28]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[218] << 1) + digits[168]) << 1) + digits[118]) << 1) + digits[68], digits[18]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[208] << 1) + digits[158]) << 1) + digits[108]) << 1) + digits[58], digits[8]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[247] << 1) + digits[197]) << 1) + digits[147]) << 1) + digits[97], digits[47]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[237] << 1) + digits[187]) << 1) + digits[137]) << 1) + digits[87], digits[37]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[227] << 1) + digits[177]) << 1) + digits[127]) << 1) + digits[77], digits[27]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[217] << 1) + digits[167]) << 1) + digits[117]) << 1) + digits[67], digits[17]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[207] << 1) + digits[157]) << 1) + digits[107]) << 1) + digits[57], digits[7]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[246] << 1) + digits[196]) << 1) + digits[146]) << 1) + digits[96], digits[46]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[236] << 1) + digits[186]) << 1) + digits[136]) << 1) + digits[86], digits[36]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[226] << 1) + digits[176]) << 1) + digits[126]) << 1) + digits[76], digits[26]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[216] << 1) + digits[166]) << 1) + digits[116]) << 1) + digits[66], digits[16]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[206] << 1) + digits[156]) << 1) + digits[106]) << 1) + digits[56], digits[6]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[245] << 1) + digits[195]) << 1) + digits[145]) << 1) + digits[95], digits[45]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[235] << 1) + digits[185]) << 1) + digits[135]) << 1) + digits[85], digits[35]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[225] << 1) + digits[175]) << 1) + digits[125]) << 1) + digits[75], digits[25]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[215] << 1) + digits[165]) << 1) + digits[115]) << 1) + digits[65], digits[15]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[205] << 1) + digits[155]) << 1) + digits[105]) << 1) + digits[55], digits[5]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[244] << 1) + digits[194]) << 1) + digits[144]) << 1) + digits[94], digits[44]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[234] << 1) + digits[184]) << 1) + digits[134]) << 1) + digits[84], digits[34]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[224] << 1) + digits[174]) << 1) + digits[124]) << 1) + digits[74], digits[24]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[214] << 1) + digits[164]) << 1) + digits[114]) << 1) + digits[64], digits[14]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[204] << 1) + digits[154]) << 1) + digits[104]) << 1) + digits[54], digits[4]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[243] << 1) + digits[193]) << 1) + digits[143]) << 1) + digits[93], digits[43]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[233] << 1) + digits[183]) << 1) + digits[133]) << 1) + digits[83], digits[33]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[223] << 1) + digits[173]) << 1) + digits[123]) << 1) + digits[73], digits[23]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[213] << 1) + digits[163]) << 1) + digits[113]) << 1) + digits[63], digits[13]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[203] << 1) + digits[153]) << 1) + digits[103]) << 1) + digits[53], digits[3]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[242] << 1) + digits[192]) << 1) + digits[142]) << 1) + digits[92], digits[42]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[232] << 1) + digits[182]) << 1) + digits[132]) << 1) + digits[82], digits[32]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[222] << 1) + digits[172]) << 1) + digits[122]) << 1) + digits[72], digits[22]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[212] << 1) + digits[162]) << 1) + digits[112]) << 1) + digits[62], digits[12]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[202] << 1) + digits[152]) << 1) + digits[102]) << 1) + digits[52], digits[2]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[241] << 1) + digits[191]) << 1) + digits[141]) << 1) + digits[91], digits[41]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[231] << 1) + digits[181]) << 1) + digits[131]) << 1) + digits[81], digits[31]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[221] << 1) + digits[171]) << 1) + digits[121]) << 1) + digits[71], digits[21]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[211] << 1) + digits[161]) << 1) + digits[111]) << 1) + digits[61], digits[11]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[201] << 1) + digits[151]) << 1) + digits[101]) << 1) + digits[51], digits[1]);
    eccmadd(S, R);

    eccdouble(R);
    table_lookup_fixed_base(S, 64 + (((((digits[240] << 1) + digits[190]) << 1) + digits[140]) << 1) + digits[90], digits[40]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 48 + (((((digits[230] << 1) + digits[180]) << 1) + digits[130]) << 1) + digits[80], digits[30]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 32 + (((((digits[220] << 1) + digits[170]) << 1) + digits[120]) << 1) + digits[70], digits[20]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 16 + (((((digits[210] << 1) + digits[160]) << 1) + digits[110]) << 1) + digits[60], digits[10]);
    eccmadd(S, R);
    table_lookup_fixed_base(S, 00 + (((((digits[200] << 1) + digits[150]) << 1) + digits[100]) << 1) + digits[50], digits[0]);
    eccmadd(S, R);

    eccnorm(R, Q);
}

static void ecc_tau(point_extproj_t P)
{ // Apply tau mapping to a point, P = tau(P)
    f2elm_t t0, t1;

    fp2sqr1271(P->x, t0);                     // t0 = X1^2
    fp2sqr1271(P->y, t1);                     // t1 = Y1^2
    fp2mul1271(P->x, P->y, P->x);             // X = X1*Y1
    fp2sqr1271(P->z, P->y);                   // Y = Z1^2
    fp2add1271(t0, t1, P->z);                 // Z = X1^2+Y1^2
    fp2sub1271(t1, t0, t0);                   // t0 = Y1^2-X1^2
    fp2add1271(P->y, P->y, P->y);             // Y = 2*Z1^2
    fp2mul1271(P->x, t0, P->x);               // X = X1*Y1*(Y1^2-X1^2)
    fp2sub1271(P->y, t0, P->y);               // Y = 2*Z1^2-(Y1^2-X1^2)
    fp2mul1271(P->x, (felm_t*)&ctau1, P->x);  // Xfinal = X*ctau1
    fp2mul1271(P->y, P->z, P->y);             // Yfinal = Y*Z
    fp2mul1271(P->z, t0, P->z);               // Zfinal = t0*Z
}

static void ecc_tau_dual(point_extproj_t P)
{ // Apply tau_dual mapping to a point, P = tau_dual(P)
    f2elm_t t0, t1;

    fp2sqr1271(P->x, t0);                          // t0 = X1^2
    fp2sqr1271(P->z, P->ta);                       // Ta = Z1^2
    fp2sqr1271(P->y, t1);                          // t1 = Y1^2
    fp2add1271(P->ta, P->ta, P->z);                // Z = 2*Z1^2
    fp2sub1271(t1, t0, P->ta);                     // Tafinal = Y1^2-X1^2
    fp2add1271(t0, t1, t0);                        // t0 = X1^2+Y1^2
    fp2mul1271(P->x, P->y, P->x);                  // X = X1*Y1
    fp2sub1271(P->z, P->ta, P->z);                 // Z = 2*Z1^2-(Y1^2-X1^2)
    fp2mul1271(P->x, (felm_t*)&ctaudual1, P->tb);  // Tbfinal = ctaudual1*X1*X1
    fp2mul1271(P->z, P->ta, P->y);                 // Yfinal = Z*Tafinal
    fp2mul1271(P->tb, t0, P->x);                   // Xfinal = Tbfinal*t0
    fp2mul1271(P->z, t0, P->z);                    // Zfinal = Z*t0
}

static void ecc_delphidel(point_extproj_t P)
{ // Apply delta_phi_delta mapping to a point, P = delta(phi_W(delta_inv(P))),
    // where phi_W is the endomorphism on the Weierstrass form
    f2elm_t t0, t1, t2, t3, t4, t5, t6;

    fp2sqr1271(P->z, t4);                          // t4 = Z1^2
    fp2mul1271(P->y, P->z, t3);                    // t3 = Y1*Z1
    fp2mul1271(t4, (felm_t*)&cphi4, t0);           // t0 = cphi4*t4
    fp2sqr1271(P->y, t2);                          // t2 = Y1^2
    fp2add1271(t0, t2, t0);                        // t0 = t0+t2
    fp2mul1271(t3, (felm_t*)&cphi3, t1);           // t1 = cphi3*t3
    fp2sub1271(t0, t1, t5);                        // t5 = t0-t1
    fp2add1271(t0, t1, t0);                        // t0 = t0+t1
    fp2mul1271(t0, P->z, t0);                      // t0 = t0*Z1
    fp2mul1271(t3, (felm_t*)&cphi1, t1);           // t1 = cphi1*t3
    fp2mul1271(t0, t5, t0);                        // t0 = t0*t5
    fp2mul1271(t4, (felm_t*)&cphi2, t5);           // t5 = cphi2*t4
    fp2add1271(t2, t5, t5);                        // t5 = t2+t5
    fp2sub1271(t1, t5, t6);                        // t6 = t1-t5
    fp2add1271(t1, t5, t1);                        // t1 = t1+t5
    fp2mul1271(t6, t1, t6);                        // t6 = t1*t6
    fp2mul1271(t6, (felm_t*)&cphi0, t6);           // t6 = cphi0*t6
    fp2mul1271(P->x, t6, P->x);                    // X = X1*t6
    fp2sqr1271(t2, t6);                            // t6 = t2^2
    fp2sqr1271(t3, t2);                            // t2 = t3^2
    fp2sqr1271(t4, t3);                            // t3 = t4^2
    fp2mul1271(t2, (felm_t*)&cphi8, t1);           // t1 = cphi8*t2
    fp2mul1271(t3, (felm_t*)&cphi9, t5);           // t5 = cphi9*t3
    fp2add1271(t1, t6, t1);                        // t1 = t1+t6
    fp2mul1271(t2, (felm_t*)&cphi6, t2);           // t2 = cphi6*t2
    fp2mul1271(t3, (felm_t*)&cphi7, t3);           // t3 = cphi7*t3
    fp2add1271(t1, t5, t1);                        // t1 = t1+t5
    fp2add1271(t2, t3, t2);                        // t2 = t2+t3
    fp2mul1271(t1, P->y, t1);                      // t1 = Y1*t1
    fp2add1271(t6, t2, P->y);                      // Y = t6+t2
    fp2mul1271(P->x, t1, P->x);                    // X = X*t1
    fp2mul1271(P->y, (felm_t*)&cphi5, P->y);       // Y = cphi5*Y
    fpneg1271(P->x[1]);                            // Xfinal = X^p
    fp2mul1271(P->y, P->z, P->y);                  // Y = Y*Z1
    fp2mul1271(t0, t1, P->z);                      // Z = t0*t1
    fp2mul1271(P->y, t0, P->y);                    // Y = Y*t0
    fpneg1271(P->z[1]);                            // Zfinal = Z^p
    fpneg1271(P->y[1]);                            // Yfinal = Y^p
}

static void ecc_delpsidel(point_extproj_t P)
{ // Apply delta_psi_delta mapping to a point, P = delta(psi_W(delta_inv(P))),
    // where psi_W is the endomorphism on the Weierstrass form
    f2elm_t t0, t1, t2;

    fpneg1271(P->x[1]);                            // X = X1^p
    fpneg1271(P->z[1]);                            // Z = Z1^p
    fpneg1271(P->y[1]);                            // Y = Y1^p
    fp2sqr1271(P->z, t2);                          // t2 = Z1^p^2
    fp2sqr1271(P->x, t0);                          // t0 = X1^p^2
    fp2mul1271(P->x, t2, P->x);                    // X = X1^p*Z1^p^2
    fp2mul1271(t2, (felm_t*)&cpsi2, P->z);         // Z = cpsi2*Z1^p^2
    fp2mul1271(t2, (felm_t*)&cpsi3, t1);           // t1 = cpsi3*Z1^p^2
    fp2mul1271(t2, (felm_t*)&cpsi4, t2);           // t2 = cpsi4*Z1^p^2
    fp2add1271(t0, P->z, P->z);                    // Z = X1^p^2 + cpsi2*Z1^p^2
    fp2add1271(t0, t2, t2);                        // t2 = X1^p^2 + cpsi4*Z1^p^2
    fp2add1271(t0, t1, t1);                        // t1 = X1^p^2 + cpsi3*Z1^p^2
    fp2neg1271(t2);                                // t2 = -(X1^p^2 + cpsi4*Z1^p^2)
    fp2mul1271(P->z, P->y, P->z);                  // Z = Y1^p*(X1^p^2 + cpsi2*Z1^p^2)
    fp2mul1271(P->x, t2, P->x);                    // X = -X1^p*Z1^p^2*(X1^p^2 + cpsi4*Z1^p^2)
    fp2mul1271(t1, P->z, P->y);                    // Yfinal = t1*Z
    fp2mul1271(P->x, (felm_t*)&cpsi1, P->x);       // Xfinal = cpsi1*X
    fp2mul1271(P->z, t2, P->z);                    // Zfinal = Z*t2
}

static void ecc_psi(point_extproj_t P)
{ // Apply psi mapping to a point, P = psi(P)
    ecc_tau(P);
    ecc_delpsidel(P);
    ecc_tau_dual(P);
}

static void ecc_phi(point_extproj_t P)
{ // Apply phi mapping to a point, P = phi(P)
    ecc_tau(P);
    ecc_delphidel(P);
    ecc_tau_dual(P);
}

static void eccneg_extproj_precomp(point_extproj_precomp_t P, point_extproj_precomp_t Q)
{ // Point negation
    copy32((uint8_t*)Q->t2, (uint8_t*)&P->t2);
    copy32((uint8_t*)Q->yx, (uint8_t*)&P->xy);
    copy32((uint8_t*)Q->xy, (uint8_t*)&P->yx);
    copy32((uint8_t*)Q->z2, (uint8_t*)&P->z2);
    fp2neg1271(Q->t2);
}

static void eccneg_precomp(point_precomp_t P, point_precomp_t Q)
{ // Point negation
    copy32((uint8_t*)Q->t2, (uint8_t*)&P->t2);
    copy32((uint8_t*)Q->yx, (uint8_t*)&P->xy);
    copy32((uint8_t*)Q->xy, (uint8_t*)&P->yx);
    fp2neg1271(Q->t2);
}

static unsigned long long mul_truncate(unsigned long long* s, unsigned long long* C)
{
    unsigned long long t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16;
    unsigned long long high00, low10, high10, low01, high01, low20, high20, low02, high02, low11, high11, low03, high03, low30, high30, low12, high12, high21;

    _umul128(s[0], C[0], &high00);
    low10 = _umul128(s[1], C[0], &high10);
    _addcarry_u64(_addcarry_u64(0, high00, low10, &t0), high10, 0, &t1);
    low01 = _umul128(s[0], C[1], &high01);
    t2 = _addcarry_u64(_addcarry_u64(0, t0, low01, &t0), t1, high01, &t3);
    low20 = _umul128(s[2], C[0], &high20);
    _addcarry_u64(_addcarry_u64(0, t3, low20, &t4), t2, high20, &t5);
    low02 = _umul128(s[0], C[2], &high02);
    t6 = _addcarry_u64(_addcarry_u64(0, t4, low02, &t7), t5, high02, &t8);
    low11 = _umul128(s[1], C[1], &high11);
    t9 = _addcarry_u64(_addcarry_u64(0, t7, low11, &t0), t8, high11, &t10);
    low03 = _umul128(s[0], C[3], &high03);
    _addcarry_u64(_addcarry_u64(0, t10, low03, &t11), t6 + t9, high03, &t12);
    low30 = _umul128(s[3], C[0], &high30);
    _addcarry_u64(_addcarry_u64(0, t11, low30, &t13), t12, high30, &t14);
    low12 = _umul128(s[1], C[2], &high12);
    _addcarry_u64(_addcarry_u64(0, t13, low12, &t15), t14, high12, &t16);

    return _addcarry_u64(0, t15, _umul128(s[2], C[1], &high21), &t0) + t16 + high21 + s[1] * C[3] + s[2] * C[2] + s[3] * C[1];
}

static void decompose(unsigned long long* k, unsigned long long* scalars)
{ // Scalar decomposition for the variable-base scalar multiplication
    const unsigned long long a1 = mul_truncate(k, (unsigned long long*)ell1);
    const unsigned long long a2 = mul_truncate(k, (unsigned long long*)ell2);
    const unsigned long long a3 = mul_truncate(k, (unsigned long long*)ell3);
    const unsigned long long a4 = mul_truncate(k, (unsigned long long*)ell4);
    scalars[0] = a1 * B11 + a2 * B21 + a3 * B31 + a4 * B41 + C1 + k[0];
    scalars[1] = a1 * B12 + a2 * B22 + a3 * B32 + a4 * B42 + C2;
    scalars[2] = a1 * B13 + a2 * B23 + a3 * B33 + a4 * B43 + C3;
    scalars[3] = a1 * B14 + a2 * B24 + a3 * B34 + a4 * B44 + C4;
    if (!(scalars[0] & 1))
    {
        scalars[0] -= B41;
        scalars[1] -= B42;
        scalars[2] -= B43;
        scalars[3] -= B44;
    }
}

static void wNAF_recode(unsigned long long scalar, unsigned int w, char* digits)
{ // Computes wNAF recoding of a scalar, where digits are in set {0,+-1,+-3,...,+-(2^(w-1)-1)}
    const int val1 = (int)(1 << (w - 1)) - 1;                           // 2^(w-1) - 1
    const int val2 = (int)(1 << w);                                     // 2^w;
    const unsigned long long mask = (unsigned long long)val2 - 1; // 2^w - 1
    int index = 0;

    while (scalar)
    {
        int digit = (int)(scalar & 1);
        if (!digit)
        {
            scalar >>= 1;                 // Shift scalar to the right by 1
            digits[index] = 0;
        }
        else
        {
            digit = (int)(scalar & mask);
            scalar >>= w;                 // Shift scalar to the right by w

            if (digit > val1)
            {
                digit -= val2;
            }
            if (digit < 0)
            {
                scalar++;                 // scalar + 1
            }
            digits[index] = digit;

            if (scalar)                   // Check if scalar != 0
            {
                for (unsigned int i = 0; i < (w - 1); i++)
                {
                    digits[++index] = 0;
                }
            }
        }
        index++;
    }

//    bs->SetMem(&digits[index], 65 - index, 0);
    memset(&digits[index], 0, 65 - index);
}

static void ecc_precomp_double(point_extproj_t P, point_extproj_precomp_t* Table)
{ // Generation of the precomputation table used internally by the double scalar multiplication function ecc_mul_double()
    point_extproj_t Q;
    point_extproj_precomp_t PP;

    R1_to_R2(P, Table[0]);                  // Precomputed point Table[0] = P in coordinates (X+Y,Y-X,2Z,2dT)
    eccdouble(P);                           // A = 2*P in (X,Y,Z,Ta,Tb)
    R1_to_R3(P, PP);                        // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,Z,T)

    eccadd_core(Table[0], PP, Q);           // Table[i] = Table[i-1]+2P using the representations (X,Y,Z,Ta,Tb) <- (X+Y,Y-X,2Z,2dT) + (X+Y,Y-X,Z,T)
    R1_to_R2(Q, Table[1]);                  // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,2Z,2dT)

    eccadd_core(Table[1], PP, Q);           // Table[i] = Table[i-1]+2P using the representations (X,Y,Z,Ta,Tb) <- (X+Y,Y-X,2Z,2dT) + (X+Y,Y-X,Z,T)
    R1_to_R2(Q, Table[2]);                  // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,2Z,2dT)

    eccadd_core(Table[2], PP, Q);           // Table[i] = Table[i-1]+2P using the representations (X,Y,Z,Ta,Tb) <- (X+Y,Y-X,2Z,2dT) + (X+Y,Y-X,Z,T)
    R1_to_R2(Q, Table[3]);                  // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,2Z,2dT)
}

static bool ecc_mul_double(unsigned long long* k, unsigned long long* l, point_t Q)
{ // Double scalar multiplication R = k*G + l*Q, where the G is the generator
    // Uses DOUBLE_SCALAR_TABLE, which contains multiples of G, Phi(G), Psi(G) and Phi(Psi(G))
    // The function uses wNAF with interleaving.
    char digits_k1[65], digits_k2[65], digits_k3[65], digits_k4[65];
    char digits_l1[65], digits_l2[65], digits_l3[65], digits_l4[65];
    point_precomp_t V;
    point_extproj_t Q1, Q2, Q3, Q4, T;
    point_extproj_precomp_t U, Q_table1[4], Q_table2[4], Q_table3[4], Q_table4[4];
    unsigned long long k_scalars[4], l_scalars[4];

    point_setup(Q, Q1);                                             // Convert to representation (X,Y,1,Ta,Tb)

    if (!ecc_point_validate(Q1))                                    // Check if point lies on the curve
    {
        return false;
    }

    // Computing endomorphisms over point Q
    copy32((uint8_t*)Q2->x, (uint8_t*)&Q1->x);
    copy32((uint8_t*)Q2->y, (uint8_t*)&Q1->y);
    copy32((uint8_t*)Q2->z, (uint8_t*)&Q1->z);
    copy32((uint8_t*)Q2->ta, (uint8_t*)&Q1->ta);
    copy32((uint8_t*)Q2->tb, (uint8_t*)&Q1->tb);
    ecc_phi(Q2);
    copy32((uint8_t*)Q3->x, (uint8_t*)&Q1->x);
    copy32((uint8_t*)Q3->y, (uint8_t*)&Q1->y);
    copy32((uint8_t*)Q3->z, (uint8_t*)&Q1->z);
    copy32((uint8_t*)Q3->ta, (uint8_t*)&Q1->ta);
    copy32((uint8_t*)Q3->tb, (uint8_t*)&Q1->tb);
    ecc_psi(Q3);
    copy32((uint8_t*)Q4->x, (uint8_t*)&Q2->x);
    copy32((uint8_t*)Q4->y, (uint8_t*)&Q2->y);
    copy32((uint8_t*)Q4->z, (uint8_t*)&Q2->z);
    copy32((uint8_t*)Q4->ta, (uint8_t*)&Q2->ta);
    copy32((uint8_t*)Q4->tb, (uint8_t*)&Q2->tb);
    ecc_psi(Q4);

    decompose((unsigned long long*)k, k_scalars);                   // Scalar decomposition
    decompose((unsigned long long*)l, l_scalars);
    wNAF_recode(k_scalars[0], 8, digits_k1);                        // Scalar recoding
    wNAF_recode(k_scalars[1], 8, digits_k2);
    wNAF_recode(k_scalars[2], 8, digits_k3);
    wNAF_recode(k_scalars[3], 8, digits_k4);
    wNAF_recode(l_scalars[0], 4, digits_l1);
    wNAF_recode(l_scalars[1], 4, digits_l2);
    wNAF_recode(l_scalars[2], 4, digits_l3);
    wNAF_recode(l_scalars[3], 4, digits_l4);
    ecc_precomp_double(Q1, Q_table1);
    ecc_precomp_double(Q2, Q_table2);
    ecc_precomp_double(Q3, Q_table3);
    ecc_precomp_double(Q4, Q_table4);

    T->x[0][0] = 0; T->x[0][1] = 0; T->x[1][0] = 0; T->x[1][1] = 0; // Initialize T as the neutral point (0:1:1)
    T->y[0][0] = 1; T->y[0][1] = 0; T->y[1][0] = 0; T->y[1][1] = 0;
    T->z[0][0] = 1; T->z[0][1] = 0; T->z[1][0] = 0; T->z[1][1] = 0;

    for (unsigned int i = 65; i--; )
    {
        eccdouble(T);

        if (digits_l1[i] < 0)
        {
            eccneg_extproj_precomp(Q_table1[(-digits_l1[i]) >> 1], U);
            eccadd(U, T);
        }
        else if (digits_l1[i] > 0)
        {
            eccadd(Q_table1[(digits_l1[i]) >> 1], T);
        }

        if (digits_l2[i] < 0)
        {
            eccneg_extproj_precomp(Q_table2[(-digits_l2[i]) >> 1], U);
            eccadd(U, T);
        }
        else if (digits_l2[i] > 0)
        {
            eccadd(Q_table2[(digits_l2[i]) >> 1], T);
        }

        if (digits_l3[i] < 0)
        {
            eccneg_extproj_precomp(Q_table3[(-digits_l3[i]) >> 1], U);
            eccadd(U, T);
        }
        else if (digits_l3[i] > 0)
        {
            eccadd(Q_table3[(digits_l3[i]) >> 1], T);
        }

        if (digits_l4[i] < 0)
        {
            eccneg_extproj_precomp(Q_table4[(-digits_l4[i]) >> 1], U);
            eccadd(U, T);
        }
        else if (digits_l4[i] > 0)
        {
            eccadd(Q_table4[(digits_l4[i]) >> 1], T);
        }

        if (digits_k1[i] < 0)
        {
            eccneg_precomp(((point_precomp_t*)&DOUBLE_SCALAR_TABLE)[(-digits_k1[i]) >> 1], V);
            eccmadd(V, T);
        }
        else if (digits_k1[i] > 0)
        {
            eccmadd(((point_precomp_t*)&DOUBLE_SCALAR_TABLE)[(digits_k1[i]) >> 1], T);
        }

        if (digits_k2[i] < 0)
        {
            eccneg_precomp(((point_precomp_t*)&DOUBLE_SCALAR_TABLE)[64 + ((-digits_k2[i]) >> 1)], V);
            eccmadd(V, T);
        }
        else if (digits_k2[i] > 0)
        {
            eccmadd(((point_precomp_t*)&DOUBLE_SCALAR_TABLE)[64 + ((digits_k2[i]) >> 1)], T);
        }

        if (digits_k3[i] < 0)
        {
            eccneg_precomp(((point_precomp_t*)&DOUBLE_SCALAR_TABLE)[2 * 64 + ((-digits_k3[i]) >> 1)], V);
            eccmadd(V, T);
        }
        else if (digits_k3[i] > 0)
        {
            eccmadd(((point_precomp_t*)&DOUBLE_SCALAR_TABLE)[2 * 64 + ((digits_k3[i]) >> 1)], T);
        }

        if (digits_k4[i] < 0)
        {
            eccneg_precomp(((point_precomp_t*)&DOUBLE_SCALAR_TABLE)[3 * 64 + ((-digits_k4[i]) >> 1)], V);
            eccmadd(V, T);
        }
        else if (digits_k4[i] > 0)
        {
            eccmadd(((point_precomp_t*)&DOUBLE_SCALAR_TABLE)[3 * 64 + ((digits_k4[i]) >> 1)], T);
        }
    }

    eccnorm(T, Q);

    return true;
}

static void ecc_precomp(point_extproj_t P, point_extproj_precomp_t* T)
{ // Generation of the precomputation table used by the variable-base scalar multiplication ecc_mul()
    point_extproj_precomp_t Q, R, S;
    point_extproj_t PP;

    // Generating Q = phi(P) = (XQ+YQ,YQ-XQ,ZQ,TQ)
    copy32((uint8_t*)PP->x, (uint8_t*)&P->x);
    copy32((uint8_t*)PP->y, (uint8_t*)&P->y);
    copy32((uint8_t*)PP->z, (uint8_t*)&P->z);
    copy32((uint8_t*)PP->ta, (uint8_t*)&P->ta);
    copy32((uint8_t*)PP->tb, (uint8_t*)&P->tb);
    ecc_phi(PP);
    R1_to_R3(PP, Q);                       // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,Z,T)

    // Generating S = psi(Q) = (XS+YS,YS-XS,ZS,TS)
    ecc_psi(PP);
    R1_to_R3(PP, S);                       // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,Z,T)

    // Generating T[0] = P = (XP+YP,YP-XP,2ZP,2dTP)
    R1_to_R2(P, T[0]);                     // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,2Z,2dT)

    // Generating R = psi(P) = (XR+YR,YR-XR,ZR,TR)
    ecc_psi(P);
    R1_to_R3(P, R);                        // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,Z,T)

    eccadd_core(T[0], Q, PP);              // T[1] = P+Q using the representations (X,Y,Z,Ta,Tb) <- (X+Y,Y-X,2Z,2dT) + (X+Y,Y-X,Z,T)
    R1_to_R2(PP, T[1]);                    // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,2Z,2dT)
    eccadd_core(T[0], R, PP);              // T[2] = P+R
    R1_to_R2(PP, T[2]);
    eccadd_core(T[1], R, PP);              // T[3] = P+Q+R
    R1_to_R2(PP, T[3]);
    eccadd_core(T[0], S, PP);              // T[4] = P+S
    R1_to_R2(PP, T[4]);
    eccadd_core(T[1], S, PP);              // T[5] = P+Q+S
    R1_to_R2(PP, T[5]);
    eccadd_core(T[2], S, PP);              // T[6] = P+R+S
    R1_to_R2(PP, T[6]);
    eccadd_core(T[3], S, PP);              // T[7] = P+Q+R+S
    R1_to_R2(PP, T[7]);
}

static void cofactor_clearing(point_extproj_t R)
{ // Co-factor clearing
    point_extproj_precomp_t Q;

    R1_to_R2(R, Q);                      // Converting from (X,Y,Z,Ta,Tb) to (X+Y,Y-X,2Z,2dT)
    eccdouble(R);                        // P = 2*P using representations (X,Y,Z,Ta,Tb) <- 2*(X,Y,Z)
    eccadd(Q, R);                        // P = P+Q using representations (X,Y,Z,Ta,Tb) <- (X,Y,Z,Ta,Tb) + (X+Y,Y-X,2Z,2dT)
    eccdouble(R);
    eccdouble(R);
    eccdouble(R);
    eccdouble(R);
    eccadd(Q, R);
    eccdouble(R);
    eccdouble(R);
    eccdouble(R);
}

static bool ecc_mul(point_t P, unsigned long long* k, point_t Q)
{ // Variable-base scalar multiplication Q = k*P using a 4-dimensional decomposition
    // This function performs point validation and (if selected) cofactor clearing
    point_extproj_t R;
    point_extproj_precomp_t Table[2][8];
    unsigned long long scalars[4];
    unsigned int digits[64], sign_masks[64];

    point_setup(P, R);                                        // Convert to representation (X,Y,1,Ta,Tb)

    if (!ecc_point_validate(R))                               // Check if point lies on the curve
    {
        return false;
    }

    decompose((unsigned long long*)k, scalars);               // Scalar decomposition

    cofactor_clearing(R);

    // Recoding sub-scalars for use in the variable-base scalar multiplication
    for (unsigned int i = 0; i < 64; i++)
    {
        scalars[0] >>= 1;
        const unsigned int bit0 = scalars[0] & 1;
        sign_masks[i] = bit0;

        digits[i] = scalars[1] & 1;
        scalars[1] = (scalars[1] >> 1) + ((bit0 | digits[i]) ^ bit0);

        unsigned int bit = scalars[2] & 1;
        scalars[2] = (scalars[2] >> 1) + ((bit0 | bit) ^ bit0);
        digits[i] += (bit << 1);

        bit = scalars[3] & 1;
        scalars[3] = (scalars[3] >> 1) + ((bit0 | bit) ^ bit0);
        digits[i] += (bit << 2);
    }

    ecc_precomp(R, Table[1]);                                 // Precomputation
    for (unsigned int i = 0; i < 8; i++)
    {
        copy32((uint8_t*)Table[0][i]->xy, (uint8_t*)Table[1][i]->yx);
        copy32((uint8_t*)Table[0][i]->yx, (uint8_t*)Table[1][i]->xy);
        copy32((uint8_t*)Table[0][i]->t2, (uint8_t*)Table[1][i]->t2);
        copy32((uint8_t*)Table[0][i]->z2, (uint8_t*)Table[1][i]->z2);
        fp2neg1271(Table[0][i]->t2);
    }
    R2_to_R4(Table[1][scalars[1] + (scalars[2] << 1) + (scalars[3] << 2)], R);

    for (unsigned int i = 64; i--; )
    {
        eccdouble(R);                                         // P = 2*P using representations (X,Y,Z,Ta,Tb) <- 2*(X,Y,Z)
        eccadd(Table[sign_masks[i]][digits[i]], R);           // P = P+S using representations (X,Y,Z,Ta,Tb) <- (X,Y,Z,Ta,Tb) + (X+Y,Y-X,2Z,2dT)
    }
    eccnorm(R, Q);                                            // Conversion to affine coordinates (x,y) and modular correction.

    return true;
}

VOID_FUNC_DECL encode(point_t P, uint8_t* Pencoded)
{ // Encode point P
    const unsigned long long temp1 = (P->x[1][1] & 0x4000000000000000) << 1;
    const unsigned long long temp2 = (P->x[0][1] & 0x4000000000000000) << 1;

    copy32(Pencoded, (uint8_t*)P->y);
    if (!P->x[0][0] && !P->x[0][1])
    {
        ((unsigned long long*)Pencoded)[3] |= temp1;
    }
    else
    {
        ((unsigned long long*)Pencoded)[3] |= temp2;
    }
}

static bool decode(const uint8_t* Pencoded, point_t P)
{ // Decode point P
    felm_t r, t, t0, t1, t2, t3, t4;
    f2elm_t u, v;
    point_extproj_t R;
    unsigned int i;
    memcpy(P->y, Pencoded, 32);
    P->y[1][1] &= 0x7FFFFFFFFFFFFFFF;

    fp2sqr1271(P->y, u);
    fp2mul1271(u, (felm_t*)&PARAMETER_d, v);
    fp2sub1271(u, (felm_t*)&ONE, u);
    fp2add1271(v, (felm_t*)&ONE, v);

    fpsqr1271(v[0], t0);                            // t0 = v0^2
    fpsqr1271(v[1], t1);                            // t1 = v1^2
    fpadd1271(t0, t1, t0);                          // t0 = t0+t1
    fpmul1271(u[0], v[0], t1);                      // t1 = u0*v0
    fpmul1271(u[1], v[1], t2);                      // t2 = u1*v1
    fpadd1271(t1, t2, t1);                          // t1 = t1+t2
    fpmul1271(u[1], v[0], t2);                      // t2 = u1*v0
    fpmul1271(u[0], v[1], t3);                      // t3 = u0*v1
    fpsub1271(t2, t3, t2);                          // t2 = t2-t3
    fpsqr1271(t1, t3);                              // t3 = t1^2
    fpsqr1271(t2, t4);                              // t4 = t2^2
    fpadd1271(t3, t4, t3);                          // t3 = t3+t4
    for (i = 0; i < 125; i++) fpsqr1271(t3, t3);    // t3 = t3^(2^125)

    fpadd1271(t1, t3, t);                           // t = t1+t3
    mod1271(t);
    if (!t[0] && !t[1])
    {
        fpsub1271(t1, t3, t);                       // t = t1-t3
    }
    fpadd1271(t, t, t);                             // t = 2*t
    fpsqr1271(t0, t3);                              // t3 = t0^2
    fpmul1271(t0, t3, t3);                          // t3 = t3*t0
    fpmul1271(t, t3, t3);                           // t3 = t3*t
    fpexp1251(t3, r);                               // r = t3^(2^125-1)
    fpmul1271(t0, r, t3);                           // t3 = t0*r
    fpmul1271(t, t3, P->x[0]);                      // x0 = t*t3
    fpsqr1271(P->x[0], t1);
    fpmul1271(t0, t1, t1);                          // t1 = t0*x0^2

    // x0 = x0/2
    unsigned long long mask, temp[2];
    mask = (0 - (1 & P->x[0][0]));
    _addcarry_u64(_addcarry_u64(0, P->x[0][0], mask, &temp[0]), P->x[0][1], (mask >> 1), &temp[1]);
    P->x[0][0] = __shiftright128(temp[0], temp[1], 1);
    P->x[0][1] = (temp[1] >> 1);

    fpmul1271(t2, t3, P->x[1]);                     // x1 = t3*t2

    fpsub1271(t, t1, t);
    mod1271(t);
    if (t[0] || t[1]) // If t != t1 then swap x0 and x1
    {
        t0[0] = P->x[0][0];
        t0[1] = P->x[0][1];
        P->x[0][0] = P->x[1][0];
        P->x[0][1] = P->x[1][1];
        P->x[1][0] = t0[0];
        P->x[1][1] = t0[1];
    }

    mod1271(P->x[0]);
    if (((unsigned int)(Pencoded[31] >> 7))
        != (unsigned int)(P->x[(!P->x[0][0] && !P->x[0][1]) ? 1 : 0][1] >> 62)) // If sign of x-coordinate decoded != input sign bit, then negate x-coordinate
    {
        fp2neg1271(P->x);
    }

    point_setup(P, R);
    if (!ecc_point_validate(R))
    {
        fpneg1271(R->x[1]);
        P->x[1][0] = R->x[1][0];
        P->x[1][1] = R->x[1][1];
        if (!ecc_point_validate(R)) // Final point validation
        {
            return false;
        }
    }

    return true;
}

VOID_FUNC_DECL signWithNonceK(const unsigned char* k, const unsigned char* publicKey, const unsigned char* messageDigest, unsigned char* signature)
{
    // Requires correctly precalculated k as input!
    // Inputs: 64-byte input (k precomputed), 32-byte publicKey, and messageDigest of size 32 in bytes
    // Output: 64-byte signature
    point_t R;
    unsigned char h[64] , temp[32 + 64];
    unsigned long long r[8];

    copy32(temp + 32, k+32);
    copy32(temp + 64, (uint8_t*)messageDigest);

    KangarooTwelve(temp + 32, 32 + 32, (unsigned char*)r, 64);

    ecc_mul_fixed(r, R);
    encode(R, signature); // Encode lowest 32 bytes of signature
    copy32(temp, signature);
    copy32(temp + 32, (uint8_t*)publicKey);

    KangarooTwelve(temp, 32 + 64, h, 64);
    Montgomery_multiply_mod_order(r, Montgomery_Rprime, r);
    Montgomery_multiply_mod_order(r, ONE, r);
    Montgomery_multiply_mod_order((unsigned long long*)h, Montgomery_Rprime, (unsigned long long*)h);
    Montgomery_multiply_mod_order((unsigned long long*)h, ONE, (unsigned long long*)h);
    Montgomery_multiply_mod_order((unsigned long long*)k, Montgomery_Rprime, (unsigned long long*)(signature + 32));
    Montgomery_multiply_mod_order((unsigned long long*)h, Montgomery_Rprime, (unsigned long long*)h);
    Montgomery_multiply_mod_order((unsigned long long*)(signature + 32), (unsigned long long*)h, (unsigned long long*)(signature + 32));
    Montgomery_multiply_mod_order((unsigned long long*)(signature + 32), ONE, (unsigned long long*)(signature + 32));
    if (_subborrow_u64(_subborrow_u64(_subborrow_u64(_subborrow_u64(0, r[0], ((unsigned long long*)signature)[4], &((unsigned long long*)signature)[4]), r[1], ((unsigned long long*)signature)[5], &((unsigned long long*)signature)[5]), r[2], ((unsigned long long*)signature)[6], &((unsigned long long*)signature)[6]), r[3], ((unsigned long long*)signature)[7], &((unsigned long long*)signature)[7]))
    {
        _addcarry_u64(_addcarry_u64(_addcarry_u64(_addcarry_u64(0, ((unsigned long long*)signature)[4], CURVE_ORDER_0, &((unsigned long long*)signature)[4]), ((unsigned long long*)signature)[5], CURVE_ORDER_1, &((unsigned long long*)signature)[5]), ((unsigned long long*)signature)[6], CURVE_ORDER_2, &((unsigned long long*)signature)[6]), ((unsigned long long*)signature)[7], CURVE_ORDER_3, &((unsigned long long*)signature)[7]);
    }
}

VOID_FUNC_DECL sign(const unsigned char* subseed, const unsigned char* publicKey, const unsigned char* messageDigest, unsigned char* signature) 
{
    // SchnorrQ signature generation
    // It produces the signature signature of a message messageDigest of size 32 in bytes
    // Inputs: 32-byte subseed, 32-byte publicKey, and messageDigest of size 32 in bytes
    // Output: 64-byte signature
    unsigned char k[64];
    KangarooTwelve((unsigned char*)subseed, 32, k, 64);
    signWithNonceK(k, publicKey, messageDigest, signature);
}

BOOL_FUNC_DECL verify(const unsigned char* publicKey, const unsigned char* messageDigest, const unsigned char* signature)
{
    point_t A;
    unsigned char temp[32 + 64];
    unsigned char h[64];

    if ((publicKey[15] & 0x80) || (signature[15] & 0x80) || (signature[62] & 0xC0) || signature[63])
    {
        return false;
    }

    if (!decode(publicKey, A)) // Also verifies that A is on the curve, if it is not it fails
    {
        return false;
    }
    memcpy(temp, signature, 32);
    memcpy(temp + 32, publicKey, 32);
    memcpy(temp + 64, messageDigest, 32);

    KangarooTwelve(temp, 32 + 64, h, 64);

    if (!ecc_mul_double((unsigned long long*)(signature + 32), (unsigned long long*)h, A))
    {
        return false;
    }

    encode(A, (unsigned char*)A);

    return (memcmp(A, signature, 32) == 0);
}

/* Get 32 bytes of public key from 55-char seed
 * */
static void getPublicKeyFromSeed(const char* seed, uint8_t* publicKey)
{
    uint8_t privateKey[32] = {0};
    uint8_t subseed[32] = {0};
    getSubseedFromSeed((uint8_t*)seed, subseed);
    getPrivateKeyFromSubSeed(subseed, privateKey);
    getPublicKeyFromPrivateKey(privateKey, publicKey);
}

/* Sign an array of bytes
 * */
static void signData(const char* seed, const uint8_t* data, const size_t dataLength, uint8_t* signature)
{
    uint8_t privateKey[32] = {0};
    uint8_t sourcePublicKey[32] = {0};
    uint8_t subseed[32] = {0};
    getSubseedFromSeed((uint8_t*)seed, subseed);
    getPrivateKeyFromSubSeed(subseed, privateKey);
    getPublicKeyFromPrivateKey(privateKey, sourcePublicKey);
    uint8_t digest[32];
    KangarooTwelve(data, uint32_t(dataLength), digest, 32);
    sign(subseed, sourcePublicKey, digest, signature);
}