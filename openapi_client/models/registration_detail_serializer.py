# coding: utf-8

"""
    Continuing Education API

    This API delivers data for the Continuing Education project.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RegistrationDetailSerializer(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'person_uuid': 'str',
        'uuid': 'str',
        'state': 'StateEnum',
        'state_text': 'str',
        'citizenship': 'str',
        'address': 'AddressSerializer',
        'registration_type': 'RegistrationTypeEnum',
        'registration_type_text': 'str',
        'use_address_for_billing': 'bool',
        'billing_address': 'AddressSerializer',
        'head_office_name': 'str',
        'company_number': 'str',
        'vat_number': 'str',
        'national_registry_number': 'str',
        'id_card_number': 'str',
        'passport_number': 'str',
        'marital_status': 'MaritalStatusEnum',
        'marital_status_text': 'str',
        'spouse_name': 'str',
        'children_number': 'int',
        'previous_ucl_registration': 'bool',
        'previous_noma': 'str',
        'use_address_for_post': 'bool',
        'residence_address': 'AddressSerializer',
        'residence_phone': 'str',
        'ucl_registration_complete': 'bool',
        'noma': 'str',
        'payment_complete': 'bool',
        'formation_spreading': 'bool',
        'prior_experience_validation': 'bool',
        'assessment_presented': 'bool',
        'assessment_succeeded': 'bool',
        'sessions': 'bool',
        'reduced_rates': 'bool',
        'spreading_payments': 'bool',
        'condition_of_acceptance': 'str'
    }

    attribute_map = {
        'person_uuid': 'person_uuid',
        'uuid': 'uuid',
        'state': 'state',
        'state_text': 'state_text',
        'citizenship': 'citizenship',
        'address': 'address',
        'registration_type': 'registration_type',
        'registration_type_text': 'registration_type_text',
        'use_address_for_billing': 'use_address_for_billing',
        'billing_address': 'billing_address',
        'head_office_name': 'head_office_name',
        'company_number': 'company_number',
        'vat_number': 'vat_number',
        'national_registry_number': 'national_registry_number',
        'id_card_number': 'id_card_number',
        'passport_number': 'passport_number',
        'marital_status': 'marital_status',
        'marital_status_text': 'marital_status_text',
        'spouse_name': 'spouse_name',
        'children_number': 'children_number',
        'previous_ucl_registration': 'previous_ucl_registration',
        'previous_noma': 'previous_noma',
        'use_address_for_post': 'use_address_for_post',
        'residence_address': 'residence_address',
        'residence_phone': 'residence_phone',
        'ucl_registration_complete': 'ucl_registration_complete',
        'noma': 'noma',
        'payment_complete': 'payment_complete',
        'formation_spreading': 'formation_spreading',
        'prior_experience_validation': 'prior_experience_validation',
        'assessment_presented': 'assessment_presented',
        'assessment_succeeded': 'assessment_succeeded',
        'sessions': 'sessions',
        'reduced_rates': 'reduced_rates',
        'spreading_payments': 'spreading_payments',
        'condition_of_acceptance': 'condition_of_acceptance'
    }

    def __init__(self, person_uuid=None, uuid=None, state=None, state_text=None, citizenship=None, address=None, registration_type=None, registration_type_text=None, use_address_for_billing=None, billing_address=None, head_office_name=None, company_number=None, vat_number=None, national_registry_number=None, id_card_number=None, passport_number=None, marital_status=None, marital_status_text=None, spouse_name=None, children_number=None, previous_ucl_registration=None, previous_noma=None, use_address_for_post=None, residence_address=None, residence_phone=None, ucl_registration_complete=None, noma=None, payment_complete=None, formation_spreading=None, prior_experience_validation=None, assessment_presented=None, assessment_succeeded=None, sessions=None, reduced_rates=None, spreading_payments=None, condition_of_acceptance=None):  # noqa: E501
        """RegistrationDetailSerializer - a model defined in OpenAPI"""  # noqa: E501

        self._person_uuid = None
        self._uuid = None
        self._state = None
        self._state_text = None
        self._citizenship = None
        self._address = None
        self._registration_type = None
        self._registration_type_text = None
        self._use_address_for_billing = None
        self._billing_address = None
        self._head_office_name = None
        self._company_number = None
        self._vat_number = None
        self._national_registry_number = None
        self._id_card_number = None
        self._passport_number = None
        self._marital_status = None
        self._marital_status_text = None
        self._spouse_name = None
        self._children_number = None
        self._previous_ucl_registration = None
        self._previous_noma = None
        self._use_address_for_post = None
        self._residence_address = None
        self._residence_phone = None
        self._ucl_registration_complete = None
        self._noma = None
        self._payment_complete = None
        self._formation_spreading = None
        self._prior_experience_validation = None
        self._assessment_presented = None
        self._assessment_succeeded = None
        self._sessions = None
        self._reduced_rates = None
        self._spreading_payments = None
        self._condition_of_acceptance = None
        self.discriminator = None

        if person_uuid is not None:
            self.person_uuid = person_uuid
        if uuid is not None:
            self.uuid = uuid
        if state is not None:
            self.state = state
        if state_text is not None:
            self.state_text = state_text
        if citizenship is not None:
            self.citizenship = citizenship
        if address is not None:
            self.address = address
        if registration_type is not None:
            self.registration_type = registration_type
        if registration_type_text is not None:
            self.registration_type_text = registration_type_text
        if use_address_for_billing is not None:
            self.use_address_for_billing = use_address_for_billing
        if billing_address is not None:
            self.billing_address = billing_address
        if head_office_name is not None:
            self.head_office_name = head_office_name
        if company_number is not None:
            self.company_number = company_number
        if vat_number is not None:
            self.vat_number = vat_number
        if national_registry_number is not None:
            self.national_registry_number = national_registry_number
        if id_card_number is not None:
            self.id_card_number = id_card_number
        if passport_number is not None:
            self.passport_number = passport_number
        if marital_status is not None:
            self.marital_status = marital_status
        if marital_status_text is not None:
            self.marital_status_text = marital_status_text
        if spouse_name is not None:
            self.spouse_name = spouse_name
        if children_number is not None:
            self.children_number = children_number
        if previous_ucl_registration is not None:
            self.previous_ucl_registration = previous_ucl_registration
        if previous_noma is not None:
            self.previous_noma = previous_noma
        if use_address_for_post is not None:
            self.use_address_for_post = use_address_for_post
        if residence_address is not None:
            self.residence_address = residence_address
        if residence_phone is not None:
            self.residence_phone = residence_phone
        if ucl_registration_complete is not None:
            self.ucl_registration_complete = ucl_registration_complete
        if noma is not None:
            self.noma = noma
        if payment_complete is not None:
            self.payment_complete = payment_complete
        if formation_spreading is not None:
            self.formation_spreading = formation_spreading
        if prior_experience_validation is not None:
            self.prior_experience_validation = prior_experience_validation
        if assessment_presented is not None:
            self.assessment_presented = assessment_presented
        if assessment_succeeded is not None:
            self.assessment_succeeded = assessment_succeeded
        if sessions is not None:
            self.sessions = sessions
        if reduced_rates is not None:
            self.reduced_rates = reduced_rates
        if spreading_payments is not None:
            self.spreading_payments = spreading_payments
        if condition_of_acceptance is not None:
            self.condition_of_acceptance = condition_of_acceptance

    @property
    def person_uuid(self):
        """Gets the person_uuid of this RegistrationDetailSerializer.  # noqa: E501


        :return: The person_uuid of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._person_uuid

    @person_uuid.setter
    def person_uuid(self, person_uuid):
        """Sets the person_uuid of this RegistrationDetailSerializer.


        :param person_uuid: The person_uuid of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._person_uuid = person_uuid

    @property
    def uuid(self):
        """Gets the uuid of this RegistrationDetailSerializer.  # noqa: E501


        :return: The uuid of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RegistrationDetailSerializer.


        :param uuid: The uuid of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def state(self):
        """Gets the state of this RegistrationDetailSerializer.  # noqa: E501


        :return: The state of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: StateEnum
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RegistrationDetailSerializer.


        :param state: The state of this RegistrationDetailSerializer.  # noqa: E501
        :type: StateEnum
        """

        self._state = state

    @property
    def state_text(self):
        """Gets the state_text of this RegistrationDetailSerializer.  # noqa: E501


        :return: The state_text of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._state_text

    @state_text.setter
    def state_text(self, state_text):
        """Sets the state_text of this RegistrationDetailSerializer.


        :param state_text: The state_text of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._state_text = state_text

    @property
    def citizenship(self):
        """Gets the citizenship of this RegistrationDetailSerializer.  # noqa: E501


        :return: The citizenship of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._citizenship

    @citizenship.setter
    def citizenship(self, citizenship):
        """Sets the citizenship of this RegistrationDetailSerializer.


        :param citizenship: The citizenship of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._citizenship = citizenship

    @property
    def address(self):
        """Gets the address of this RegistrationDetailSerializer.  # noqa: E501


        :return: The address of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: AddressSerializer
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RegistrationDetailSerializer.


        :param address: The address of this RegistrationDetailSerializer.  # noqa: E501
        :type: AddressSerializer
        """

        self._address = address

    @property
    def registration_type(self):
        """Gets the registration_type of this RegistrationDetailSerializer.  # noqa: E501


        :return: The registration_type of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: RegistrationTypeEnum
        """
        return self._registration_type

    @registration_type.setter
    def registration_type(self, registration_type):
        """Sets the registration_type of this RegistrationDetailSerializer.


        :param registration_type: The registration_type of this RegistrationDetailSerializer.  # noqa: E501
        :type: RegistrationTypeEnum
        """

        self._registration_type = registration_type

    @property
    def registration_type_text(self):
        """Gets the registration_type_text of this RegistrationDetailSerializer.  # noqa: E501


        :return: The registration_type_text of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._registration_type_text

    @registration_type_text.setter
    def registration_type_text(self, registration_type_text):
        """Sets the registration_type_text of this RegistrationDetailSerializer.


        :param registration_type_text: The registration_type_text of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._registration_type_text = registration_type_text

    @property
    def use_address_for_billing(self):
        """Gets the use_address_for_billing of this RegistrationDetailSerializer.  # noqa: E501


        :return: The use_address_for_billing of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._use_address_for_billing

    @use_address_for_billing.setter
    def use_address_for_billing(self, use_address_for_billing):
        """Sets the use_address_for_billing of this RegistrationDetailSerializer.


        :param use_address_for_billing: The use_address_for_billing of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._use_address_for_billing = use_address_for_billing

    @property
    def billing_address(self):
        """Gets the billing_address of this RegistrationDetailSerializer.  # noqa: E501


        :return: The billing_address of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: AddressSerializer
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this RegistrationDetailSerializer.


        :param billing_address: The billing_address of this RegistrationDetailSerializer.  # noqa: E501
        :type: AddressSerializer
        """

        self._billing_address = billing_address

    @property
    def head_office_name(self):
        """Gets the head_office_name of this RegistrationDetailSerializer.  # noqa: E501


        :return: The head_office_name of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._head_office_name

    @head_office_name.setter
    def head_office_name(self, head_office_name):
        """Sets the head_office_name of this RegistrationDetailSerializer.


        :param head_office_name: The head_office_name of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._head_office_name = head_office_name

    @property
    def company_number(self):
        """Gets the company_number of this RegistrationDetailSerializer.  # noqa: E501


        :return: The company_number of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._company_number

    @company_number.setter
    def company_number(self, company_number):
        """Sets the company_number of this RegistrationDetailSerializer.


        :param company_number: The company_number of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._company_number = company_number

    @property
    def vat_number(self):
        """Gets the vat_number of this RegistrationDetailSerializer.  # noqa: E501


        :return: The vat_number of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """Sets the vat_number of this RegistrationDetailSerializer.


        :param vat_number: The vat_number of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._vat_number = vat_number

    @property
    def national_registry_number(self):
        """Gets the national_registry_number of this RegistrationDetailSerializer.  # noqa: E501


        :return: The national_registry_number of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._national_registry_number

    @national_registry_number.setter
    def national_registry_number(self, national_registry_number):
        """Sets the national_registry_number of this RegistrationDetailSerializer.


        :param national_registry_number: The national_registry_number of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._national_registry_number = national_registry_number

    @property
    def id_card_number(self):
        """Gets the id_card_number of this RegistrationDetailSerializer.  # noqa: E501


        :return: The id_card_number of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._id_card_number

    @id_card_number.setter
    def id_card_number(self, id_card_number):
        """Sets the id_card_number of this RegistrationDetailSerializer.


        :param id_card_number: The id_card_number of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._id_card_number = id_card_number

    @property
    def passport_number(self):
        """Gets the passport_number of this RegistrationDetailSerializer.  # noqa: E501


        :return: The passport_number of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._passport_number

    @passport_number.setter
    def passport_number(self, passport_number):
        """Sets the passport_number of this RegistrationDetailSerializer.


        :param passport_number: The passport_number of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._passport_number = passport_number

    @property
    def marital_status(self):
        """Gets the marital_status of this RegistrationDetailSerializer.  # noqa: E501


        :return: The marital_status of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: MaritalStatusEnum
        """
        return self._marital_status

    @marital_status.setter
    def marital_status(self, marital_status):
        """Sets the marital_status of this RegistrationDetailSerializer.


        :param marital_status: The marital_status of this RegistrationDetailSerializer.  # noqa: E501
        :type: MaritalStatusEnum
        """

        self._marital_status = marital_status

    @property
    def marital_status_text(self):
        """Gets the marital_status_text of this RegistrationDetailSerializer.  # noqa: E501


        :return: The marital_status_text of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._marital_status_text

    @marital_status_text.setter
    def marital_status_text(self, marital_status_text):
        """Sets the marital_status_text of this RegistrationDetailSerializer.


        :param marital_status_text: The marital_status_text of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._marital_status_text = marital_status_text

    @property
    def spouse_name(self):
        """Gets the spouse_name of this RegistrationDetailSerializer.  # noqa: E501


        :return: The spouse_name of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._spouse_name

    @spouse_name.setter
    def spouse_name(self, spouse_name):
        """Sets the spouse_name of this RegistrationDetailSerializer.


        :param spouse_name: The spouse_name of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._spouse_name = spouse_name

    @property
    def children_number(self):
        """Gets the children_number of this RegistrationDetailSerializer.  # noqa: E501


        :return: The children_number of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: int
        """
        return self._children_number

    @children_number.setter
    def children_number(self, children_number):
        """Sets the children_number of this RegistrationDetailSerializer.


        :param children_number: The children_number of this RegistrationDetailSerializer.  # noqa: E501
        :type: int
        """

        self._children_number = children_number

    @property
    def previous_ucl_registration(self):
        """Gets the previous_ucl_registration of this RegistrationDetailSerializer.  # noqa: E501


        :return: The previous_ucl_registration of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._previous_ucl_registration

    @previous_ucl_registration.setter
    def previous_ucl_registration(self, previous_ucl_registration):
        """Sets the previous_ucl_registration of this RegistrationDetailSerializer.


        :param previous_ucl_registration: The previous_ucl_registration of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._previous_ucl_registration = previous_ucl_registration

    @property
    def previous_noma(self):
        """Gets the previous_noma of this RegistrationDetailSerializer.  # noqa: E501


        :return: The previous_noma of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._previous_noma

    @previous_noma.setter
    def previous_noma(self, previous_noma):
        """Sets the previous_noma of this RegistrationDetailSerializer.


        :param previous_noma: The previous_noma of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._previous_noma = previous_noma

    @property
    def use_address_for_post(self):
        """Gets the use_address_for_post of this RegistrationDetailSerializer.  # noqa: E501


        :return: The use_address_for_post of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._use_address_for_post

    @use_address_for_post.setter
    def use_address_for_post(self, use_address_for_post):
        """Sets the use_address_for_post of this RegistrationDetailSerializer.


        :param use_address_for_post: The use_address_for_post of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._use_address_for_post = use_address_for_post

    @property
    def residence_address(self):
        """Gets the residence_address of this RegistrationDetailSerializer.  # noqa: E501


        :return: The residence_address of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: AddressSerializer
        """
        return self._residence_address

    @residence_address.setter
    def residence_address(self, residence_address):
        """Sets the residence_address of this RegistrationDetailSerializer.


        :param residence_address: The residence_address of this RegistrationDetailSerializer.  # noqa: E501
        :type: AddressSerializer
        """

        self._residence_address = residence_address

    @property
    def residence_phone(self):
        """Gets the residence_phone of this RegistrationDetailSerializer.  # noqa: E501


        :return: The residence_phone of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._residence_phone

    @residence_phone.setter
    def residence_phone(self, residence_phone):
        """Sets the residence_phone of this RegistrationDetailSerializer.


        :param residence_phone: The residence_phone of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._residence_phone = residence_phone

    @property
    def ucl_registration_complete(self):
        """Gets the ucl_registration_complete of this RegistrationDetailSerializer.  # noqa: E501


        :return: The ucl_registration_complete of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._ucl_registration_complete

    @ucl_registration_complete.setter
    def ucl_registration_complete(self, ucl_registration_complete):
        """Sets the ucl_registration_complete of this RegistrationDetailSerializer.


        :param ucl_registration_complete: The ucl_registration_complete of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._ucl_registration_complete = ucl_registration_complete

    @property
    def noma(self):
        """Gets the noma of this RegistrationDetailSerializer.  # noqa: E501


        :return: The noma of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._noma

    @noma.setter
    def noma(self, noma):
        """Sets the noma of this RegistrationDetailSerializer.


        :param noma: The noma of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._noma = noma

    @property
    def payment_complete(self):
        """Gets the payment_complete of this RegistrationDetailSerializer.  # noqa: E501


        :return: The payment_complete of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._payment_complete

    @payment_complete.setter
    def payment_complete(self, payment_complete):
        """Sets the payment_complete of this RegistrationDetailSerializer.


        :param payment_complete: The payment_complete of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._payment_complete = payment_complete

    @property
    def formation_spreading(self):
        """Gets the formation_spreading of this RegistrationDetailSerializer.  # noqa: E501


        :return: The formation_spreading of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._formation_spreading

    @formation_spreading.setter
    def formation_spreading(self, formation_spreading):
        """Sets the formation_spreading of this RegistrationDetailSerializer.


        :param formation_spreading: The formation_spreading of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._formation_spreading = formation_spreading

    @property
    def prior_experience_validation(self):
        """Gets the prior_experience_validation of this RegistrationDetailSerializer.  # noqa: E501


        :return: The prior_experience_validation of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._prior_experience_validation

    @prior_experience_validation.setter
    def prior_experience_validation(self, prior_experience_validation):
        """Sets the prior_experience_validation of this RegistrationDetailSerializer.


        :param prior_experience_validation: The prior_experience_validation of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._prior_experience_validation = prior_experience_validation

    @property
    def assessment_presented(self):
        """Gets the assessment_presented of this RegistrationDetailSerializer.  # noqa: E501


        :return: The assessment_presented of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._assessment_presented

    @assessment_presented.setter
    def assessment_presented(self, assessment_presented):
        """Sets the assessment_presented of this RegistrationDetailSerializer.


        :param assessment_presented: The assessment_presented of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._assessment_presented = assessment_presented

    @property
    def assessment_succeeded(self):
        """Gets the assessment_succeeded of this RegistrationDetailSerializer.  # noqa: E501


        :return: The assessment_succeeded of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._assessment_succeeded

    @assessment_succeeded.setter
    def assessment_succeeded(self, assessment_succeeded):
        """Sets the assessment_succeeded of this RegistrationDetailSerializer.


        :param assessment_succeeded: The assessment_succeeded of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._assessment_succeeded = assessment_succeeded

    @property
    def sessions(self):
        """Gets the sessions of this RegistrationDetailSerializer.  # noqa: E501


        :return: The sessions of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """Sets the sessions of this RegistrationDetailSerializer.


        :param sessions: The sessions of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._sessions = sessions

    @property
    def reduced_rates(self):
        """Gets the reduced_rates of this RegistrationDetailSerializer.  # noqa: E501


        :return: The reduced_rates of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._reduced_rates

    @reduced_rates.setter
    def reduced_rates(self, reduced_rates):
        """Sets the reduced_rates of this RegistrationDetailSerializer.


        :param reduced_rates: The reduced_rates of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._reduced_rates = reduced_rates

    @property
    def spreading_payments(self):
        """Gets the spreading_payments of this RegistrationDetailSerializer.  # noqa: E501


        :return: The spreading_payments of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._spreading_payments

    @spreading_payments.setter
    def spreading_payments(self, spreading_payments):
        """Sets the spreading_payments of this RegistrationDetailSerializer.


        :param spreading_payments: The spreading_payments of this RegistrationDetailSerializer.  # noqa: E501
        :type: bool
        """

        self._spreading_payments = spreading_payments

    @property
    def condition_of_acceptance(self):
        """Gets the condition_of_acceptance of this RegistrationDetailSerializer.  # noqa: E501


        :return: The condition_of_acceptance of this RegistrationDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._condition_of_acceptance

    @condition_of_acceptance.setter
    def condition_of_acceptance(self, condition_of_acceptance):
        """Sets the condition_of_acceptance of this RegistrationDetailSerializer.


        :param condition_of_acceptance: The condition_of_acceptance of this RegistrationDetailSerializer.  # noqa: E501
        :type: str
        """

        self._condition_of_acceptance = condition_of_acceptance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegistrationDetailSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
